import jinja2
import jinja2.ext
import jinja2.nodes
import yaml

class Query:

    def __init__(self, template_env, connection, raw_query, defaults=None):
        self.template_env = template_env
        self.connection = connection
        self.raw_query = raw_query
        self.defaults = defaults or {}
        self.context = dict()

    def render(self, **kwargs):
        self.template = self.template_env.from_string(self.raw_query)
        self.template.globals['query'] = self._include_query
        self.reset_context()
        self.update_context(kwargs)
        cp = {}
        cp.update(self.context)
        return self.template.render(cp)

    def reset_context(self):
        self.context.clear()
        self.context.update(self.defaults)

    def update_context(self, context):
        self.context.update(context)

    def __call__(self, **kwargs):
        sql = self.render(**kwargs)
        return self.execute(sql, **self.context)

    def one(self, **kwargs):
        return next(self(**kwargs))

    def value(self, **kwargs):
        return self.one(**kwargs)[0]

    def execute(self, sql, mode='list', **params):
        raise NotImplementedError()

    def _include_query(self, name):
        query = self.template_env.queries[name]
        for default, value in query.defaults.items():
            if default not in self.context:
                self.context[default] = value
        return query.render(**self.context)

class PostgresQuery(Query):
    def execute(self, sql, mode='list', **params):
        cur = self.connection.cursor()
        cur.execute(sql, params)

        for record in cur:
            yield record

class Dao:
    def __init__(self, connection, query_class=PostgresQuery):
        self.connection = connection
        self.query_class = query_class
        self.template_env = jinja2.Environment()
        self.template_env.queries = self

        self.queries = {}

    def load(self, query_file_path):
        with open(query_file_path) as qf:
            for name, desc in yaml.load(qf).items():
                self.queries[name] = self.create_query_from_desc(desc)


    def create_query_from_desc(self, desc):
        defaults = {}
        if isinstance(desc, dict):
            sql, defaults = desc['query'], desc['defaults']
        else:
            sql = desc

        return self.query_class(
            self.template_env,
            self.connection,
            sql,
            defaults=defaults
        )

    def __getattr__(self, name):
        try:
            return self.queries[name]
        except KeyError:
            return getattr(super(), name)


    def __getitem__(self, name):
        return self.__getattr__(name)
