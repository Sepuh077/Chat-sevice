$(document).ready(function() {
    var group_id = window.location.href.split('chat/')[1].split('/')[0]
    $(document).on('click', '.reply-msg', function() {
        $("#replied-from").html($(this).attr('value'))
    })
})