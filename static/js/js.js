/**
 * Created by ripundeep on 30/1/16.
 */

 angular.module("signupapp", [])
     .controller("signupcontroller",function($scope,$http) {
         $scope.user_info = {
             'username': null,
             'first_name':null,
             'last_name':null,
             'agree':'False',
             'pwd':null,
             'cpwd':null,
             'email':null
         };

         $scope.signup=function(){
             var req = {
                 url: 'signup',
                 method:'POST',
                 data: $scope.user_info
             }
             $http(req).success( function(response) {
                 window.alert(response);
            })
         }
         $scope.login = function () {
           window.location.href = 'login';
         }

     });

angular.module("loginapp", [])
     .controller("logincontroller",['$scope','$http', function($scope,$http) {
         $scope.login_info = {
             'username': null,
             'pwd':null,
         };
         $scope.login=function(){
             var req = {
                 url: '/dashboard/check_auth',
                 method:'POST',
                 data: $scope.login_info
             }
             $http(req).success( function(response) {
                 window.alert(response)
            })
         }
         //$scope.signup = function () {
         //  window.location.href = 'signup';
         //}

     }]);
//angular.module("homeapp",[])
//    .controller("homecontroller",['$http','$scope',function($http,$scope){
//        $scope.logout=function(){
//            var req = {
//                url:'/stockportfolio/logout',
//                method:'POST'
//            }
//            $http(req).success(function(response){
//                window.alert(response);
//                window.location.href = 'signup';
//            })
//            $http(req).error(function(response){
//                window.alert(response);
//            })
//
//        }
//
//    }]);




