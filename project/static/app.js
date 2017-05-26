$(".btn-success").click(function() {
    $("#todo").append("<li>" + $("input[name=task]").val() + " <a href='#' class='close' aria-hidden='true'>&times;</a></li>");
})

$("body").on('click', '#todo a', function() {
    $(this).closest("li").remove();
});