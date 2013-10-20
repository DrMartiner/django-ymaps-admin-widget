module.exports = (grunt) ->
    grunt.initConfig
        pkg: grunt.file.readJSON 'package.json'
        watch:
            coffee:
                files: ['yandexmaps_widget/static/coffee/**/*.coffee']
                tasks: ['coffee:dist']
        coffee:
            dist:
                files: [{
                    expand: true,
                    cwd: 'yandexmaps_widget/static/coffee',
                    src: '**/*.coffee',
                    dest: 'yandexmaps_widget/static/js',
                    ext: '.js'
                }]
    grunt.loadNpmTasks 'grunt-contrib-coffee'
    grunt.loadNpmTasks 'grunt-contrib-watch'

    grunt.registerTask 'run', [
        'coffee:dist',
        'watch'
    ]