$(document).ready(function () {
    var group_id = window.location.href.split('chat/')[1].split('/')[0]
    var last_msg_date
    const msg_count_per_request = 10
    let is_all_received = false
    let can_get_next = false
    let user_id

    function create_message_html(message) {
        return `<div class="message-info-container" ${message['sender']['id'] == user_id ? 'style="align-items: flex-end;"' : ''}>
                    <div class="message-info">
                        <div class="message-text">
                            <div class="message-header">
                                ${message['sender']['name']}
                            </div>
                            ${message['text']}
                            <div class="message-sent-time">
                                ${message['sent_time']}
                            </div>
                            <div class='msg-buttons'>
                                <div class='reply-msg' value='${message['id']}'>
                                    Reply
                                </div>
                            </div>
                        </div>
                    </div>
                </div>`
    }

    function get_scroll_position(new_pos=null) {
        if(new_pos) {
            $('#messages-container').scrollTop(new_pos)
        }

        return $('#messages-container').scrollTop()
    }

    function get_messages() {
        can_get_next = false
        // var x = new Date()
        // console.log(x.getUTCHours() + ':' + x.getUTCMinutes())
        // for(let i = 0; i < 100000000; ++i) {
        //     let x
        // }
        if(is_all_received) {
            return
        }
        return $.ajax({
            method: 'GET',
            url: `/chat/get-messages/${group_id}/`,
            dataType: 'json',
            data: {
                'count': $('.message-info-container').length,
                'msg_count': msg_count_per_request
            },
            success: function (data) {
                user_id = data['user_id']
                let messages = data['messages']
                let message_count = 0
                
                let html_code = ''
                for(let [msg_date, msg_info] of Object.entries(messages)) {
                    for(let i = 0; i < msg_info.length; ++i) {
                        html_code += create_message_html(msg_info[i])
                        message_count++
                    }
                    html_code += `<div class="date-container">
                                        <div class="date">
                                            ${msg_date}
                                        </div>
                                    </div>`
                    if(msg_date == last_msg_date) {
                        $('#messages > .date-container:last-child()').remove()
                    }
                    last_msg_date = msg_date
                }
                if(message_count < msg_count_per_request) {
                    is_all_received = true
                }
                let scroll_pos = get_scroll_position()
                $('#messages').html($('#messages').html() + html_code)
                get_scroll_position(scroll_pos)
                can_get_next = true
            }
        })
    }

    $('#messages-container').scroll(function(e) {
        // $(this).scrollTop().valueOf() this value is < 0
        // $('#messages').innerHeight()
        // $(this).height()
        if($('#messages').innerHeight() + $(this).scrollTop().valueOf() <= 200 + $(this).height() && can_get_next && !is_all_received) {
            get_messages()
        }
    })

    get_messages()
})