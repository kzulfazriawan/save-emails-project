module.exports = function($scope, $timeout, $window, Http){
    $scope.alert = null;
    $scope.error = null;
    $scope.data  = null;
    $scope.form  = {
        event_id: null,
        email_subject: null,
        email_content: null,
        timestamp: null
    }
    $scope.select = [];

    $scope.get = function(){
        let target = '/save_emails';

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

    $scope.event = function(){
        let target = '/event';

        Http.sendGet(target).then(
            function success(response){
                $scope.select = response.data;
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
        let tmp_timestamp = new Date($scope.form.timestamp);
        let timestamps_date = tmp_timestamp.getFullYear() + "-" + parseInt(tmp_timestamp.getMonth()+1) + "-" + tmp_timestamp.getDate()
        timestamps_date += " " + tmp_timestamp.getHours() + ":" + tmp_timestamp.getMinutes() + ":00";

        var tmp_data = $scope.form;
        tmp_data.timestamp = timestamps_date

        // ____sending post to login API____
        let method = 'POST';
        let target = '/save_emails';
        let data   = {data: tmp_data};

        Http.sendAsJson(method, target, data).then(
            function success(response){
                console.log(response);
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