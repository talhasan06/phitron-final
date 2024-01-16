$(document).ready(function () {
    function loadContent(url) {
        $('#dynamicContentContainer').load(url);
    }

    $('#allTasksButton').on('click', function (e) {
        e.preventDefault();
        loadContent($(this).attr('href'));
    });

    $('#completedButton').on('click', function (e) {
        e.preventDefault();
        loadContent($(this).attr('href'));
    });

    $('#pendingButton').on('click', function (e) {
        e.preventDefault();
        loadContent($(this).attr('href'));
    });

    $('#dueDateSort').on('click', function (e) {
        e.preventDefault();
        loadContent($(this).attr('href'));
    });

});