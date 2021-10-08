module.exports = function($scope, $timeout, $window, Http){
    $scope.alert = null;
    $scope.error = null;
    $scope.data  = null;
    $scope.form  = {
        name : null,
        email: null
    }

    $scope.get = function(){
        let target = '/emails';

        Http.sendGet(target).then(
            function success(response){
                $scope.data = response.data;
                console.log(response);
            },

            function error(response){
                $scope.alert = {
                    class: 'danger',
                    msg: 'Error when loading'
                }
            }
        )
    }

    $scope.post = function(){
        // ____sending post to login API____
        let method = 'POST';
        let target = '/emails';
        let data   = {data: $scope.form};

        Http.sendAsJson(method, target, data).then(
            function success(response){
                $timeout(function(){
                    $window.location.href = '/';
                });
            },

            function error(response){
                $scope.alert = {
                    class: 'danger',
                    msg: 'Error when saving'
                }
            }
        )
    }
}