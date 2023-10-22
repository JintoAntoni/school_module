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

    $(document).ready(function () {
                $('.student_class').click(function(ev){
                    console.log("-----------------",$('.student_class'))
                    $('.student_class').removeClass('active').css('background-color','unset')
                    console.log("GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",ev)
                    $(ev.currentTarget).addClass('active').css('background-color','darkgray')
                })
                 var tableRow = $('.student_class')
                 console.log("Table Row---->>",tableRow)
                 var arrayRows = Array.from(tableRow);
                 console.log("arrayRows------->>",arrayRows)




});
});