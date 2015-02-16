// Angular main module

var app = angular.module('notebook', []);

app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
});

app.controller('TimelineController', function() {
    this.articles = 'Here will be the articles';

});

app.controller('TabController', function() {
    this.activeTab = 1;

    this.selectTab = function(tab) {
        this.activeTab = tab;
    };

    this.isSelected = function(tab) {
        return this.activeTab === tab;
    };

});