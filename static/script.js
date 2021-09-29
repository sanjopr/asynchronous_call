$(function () {
    $('a#async').bind('click', function () {
        $.getJSON('/async', function (data) {
            $("input:text").val(data.time);
            $("#result_json_textarea").val(JSON.stringify(data.results));
        });
        return false;
    });
    $('a#sync').bind('click', function () {
        $.getJSON('/sync', function (data) {

            $("input:text").val(data.time);
            $("#result_json_textarea").val(JSON.stringify(data.results));
        });
        return false;
    });
    var $loading = $('#loading-div').hide();
    $(document)
        .ajaxStart(function () {
            $loading.show();
        })
        .ajaxStop(function () {
            $loading.hide();
        });
});