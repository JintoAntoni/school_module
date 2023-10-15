odoo.define('school_module.website',
    function (require) {
    "use strict";
    var ajax = require('web.ajax');

    $('.del_student').on('click',function(){
    var cardTitle = this.closest('.card-body').querySelector('.card-title').textContent;
    console.log(cardTitle)
    ajax.jsonRpc('/delete_student', 'call', {
                        'student_name':  cardTitle,
                    }).then(function (data) {
                    console.log("result",data)
                    });

    });

});
