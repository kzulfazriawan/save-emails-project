module.exports = function($scope, $timeout, $window, Http){
    $scope.alert = null;
    $scope.error = null;
    $scope.data  = null;
    $scope.form  = {
        name : null,
        description: null
    }

    $scope.get = function(){
        let target = '/event';

        Http.sendGet(target).then(
            function success(response){
                $scope.data = response.data;
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
        let target = '/event';
        let data   = {data: $scope.form};

        Http.sendAsJson(method, target, data).then(
            function success(response){
                $timeout(function(){
                    $window.location.reload();
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