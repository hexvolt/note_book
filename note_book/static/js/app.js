// Angular main module

var app = angular.module('notebook', []);

app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
});

app.controller('TimelineController', function() {
    this.articles = 'Here will be the articles';

});