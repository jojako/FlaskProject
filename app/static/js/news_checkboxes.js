$(document).ready(function () {
    $("#news_table #checkall").click(function () {
        if ($("#news_table #checkall").is(':checked')) {
            $("#news_table input[type=checkbox]").each(function () {
                $(this).prop("checked", true);
            });

        } else {
            $("#news_table input[type=checkbox]").each(function () {
                $(this).prop("checked", false);
            });
        }
    });

});
