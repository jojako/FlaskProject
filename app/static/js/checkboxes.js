
$(document).ready(function () {
    $("#user_table #checkall").click(function () {
        if ($("#user_table #checkall").is(':checked')) {
            $("#user_table input[type=checkbox]").each(function () {
                $(this).prop("checked", true);
            });

        } else {
            $("#user_table input[type=checkbox]").each(function () {
                $(this).prop("checked", false);
            });
        }
    });

});