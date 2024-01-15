$(document).ready(function () {
    $('#allTasksButton').on('click', function (e) {
        e.preventDefault();
        $('#dynamicContentContainer').load($(this).attr('href'));
    });
});
$(document).ready(function () {
    $('#completedButton').on('click', function (e) {
        e.preventDefault();
        $('#dynamicContentContainer').load($(this).attr('href'));
    });
});
$(document).ready(function () {
    $('#pendingButton').on('click', function (e) {
        e.preventDefault();
        $('#dynamicContentContainer').load($(this).attr('href'));
    });
});
$(document).ready(function () {
    $('#pendingButton').on('click', function (e) {
        e.preventDefault();
        $('#dynamicContentContainer').load($(this).attr('href'));
    });
});