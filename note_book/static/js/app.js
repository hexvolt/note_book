// Angular main module

var app = angular.module('notebook', ['controllers']);

app.config(function($interpolateProvider) {
    // changing the default brackets
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
});
