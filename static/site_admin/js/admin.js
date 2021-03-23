$(document).ready(function () {
    // Creating a form for the delivery selection
    $("#select-go").click(function () {
        var actionSelected = $("#select-options option:selected").val();
        var fieldsSelected = [];
        $.each($(".order-checks:checkbox:checked"), function () {
            fieldsSelected.push($(this).attr("id"));
            $('#id-selected').val(fieldsSelected);
        });

        if (actionSelected == "dispatched") {
            $("#select-form").attr('action', "/site-admin/dispatch/");
            $("#select-form").submit();
        } else if (actionSelected == "completed") {
            $("#select-form").attr('action', "/site-admin/complete/");
            $("#select-form").submit();
        };
    });
});