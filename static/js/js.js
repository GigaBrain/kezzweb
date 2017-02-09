/**
 * Created by ripundeep on 30/1/16.
 */

 angular.module("adduserapp", [])
     .controller("addusercontroller",function($scope,$http) {
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
                 url: '/dashboard/add_user',
                 method:'POST',
                 data: $scope.user_info
             }
             $http(req).success( function(response) {
                 if (response=="200"){
                    window.location.href = "/dashboard/home"
                }
                 else{
                     window.location.href = "Failure"
                 }
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
                 url: '/dashboard/login',
                 method:'POST',
                 data: $scope.login_info
             }
             $http(req).success( function(response) {

            })
         }

     }]);

angular.module("templateapp",[])
    .controller("templatecontroller",['$http','$scope',function($http,$scope){
        $scope.logout=function(){
            var req = {
                url:'/dashboard/logout',
                method:'POST'
            }
            $http(req).success(function(response){
                if (response=="200"){
                    window.location.href = "/dashboard/login"
                }

            })
            $http(req).error(function(response){
                window.alert(response);
            })

        }

    }]);

angular.module("containerapp",[])
    .controller("containercontroller",['$http','$scope',function($http,$scope){
        $scope.add_user=function(){
            var req = {
                url:'/dashboard/logout',
                method:'POST'
            }
            $http(req).success(function(response){
                if (response=="200"){
                    window.location.href = "/dashboard/login"
                }

            })
            $http(req).error(function(response){
                window.alert(response);
            })

        }

    }]);





