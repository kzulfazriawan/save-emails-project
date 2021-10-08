// Angularjs require
var angular = require('angular');
require('angular-route');
require('ng-file-upload');
require('angular-sanitize');


// AngularJS module working
var app = angular.module('App', ['ngRoute', 'ngFileUpload', 'ngSanitize']);

// Factories
app.factory('Http', require('./http'));

// Controllers
app.controller('Email', require('./controllers/email'));