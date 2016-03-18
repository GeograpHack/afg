'use strict';

var gulp = require('gulp'),
    plumber = require('gulp-plumber'),
    sass = require('gulp-sass'),
    notify = require('gulp-notify'),
    prefixer = require('gulp-autoprefixer'),
    livereload = require('gulp-livereload'),
    path = require('path'),
    fs = require('fs');

var bowerDir = 'afg/static/vendor',
    sassPath = 'afg/static/style/style.scss',
    sassOutput = 'afg/static/style/generated',
    sassLoadPath = [
        sassPath,
        bowerDir + '/Materialize/sass'
    ],
    watchPath = [
        'afg/static/style/*.scss',
        bowerDir + '/**/*.scss'
    ];
console.log(sassPath, bowerDir, sassLoadPath)
gulp.task('sass', function() {
    gulp.src(sassPath)
        .pipe(plumber())
        .pipe(sass({
            style: 'compressed',
            includePaths: sassLoadPath
        }))
        .pipe(prefixer({
            browser: ['last 2 versions'],
            cascade: false
        }))
        .pipe(gulp.dest(sassOutput))
        .pipe(plumber.stop())
        .pipe(livereload())
});

gulp.task('sass:watch', function() {
    livereload.listen();
    gulp.watch(watchPath, ['sass']);
})

gulp.task('default', ['sass'])
