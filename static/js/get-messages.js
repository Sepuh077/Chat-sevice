$(document).ready(function () {
    var group_id = window.location.href.split('chat/')[1].split('/')[0]
    var msg_dates = []

    function create_message_html(message) {
        return `<div class="message-info-container" style="align-items: flex-end;">
                <div class="message-info">
                    <div class="message-text">
                        <div class="message-header">
                            ${message['sender']['name']}
                        </div>
                        ${message['text']}
                        <div class="message-sent-time">
                            ${message['sent_time'].split('|')[1]}
                        </div>
                    </div>
                </div>
            </div>`
    }

    function get_messages() {
        $.ajax({
            method: 'GET',
            url: `/chat/get-messages/${group_id}/`,
            dataType: 'json',
            success: function (data) {
                let user_id = data['user_id']
                let messages = data['messages']
                
                let html_code = ''
                for(let i = 0; i < messages.length; ++i) {
                    let date = messages[i]['sent_time'].split('|')[0]
                    if(!msg_dates.includes(date)) {
                        html_code += `<div class="date-container">
                                        <div class="date">
                                            ${date}
                                        </div>
                                    </div>`
                        msg_dates.push(date)
                    }
                    html_code += create_message_html(messages[i])
                }

                $('#messages').html(html_code)
            }
        })
    }

    get_messages()
})