$(document).ready(function(){

    var getPortfolios = function getPortfolios(data){
        $.get("/portfolio/show_list",function(data){
                    console.log(data);
                    var template = $('#list_template').html();
                    var rendered = Mustache.render(template,data);
                    $('div.list_portfolios').html(rendered);
                  
                });
        }
    $('.list_portfolios').on('click','.update_link', function(event){ 
            event.preventDefault(); 
            var $a = $(this);
                var path = $a.attr('id');
                var data = {res : path} ;
            $.get( "/portfolio/update/"+path, $(this).serialize(), function(data){
                var template = $('#update_template').html();
                var rendered = Mustache.render(template,data);
                $('.update_class_form').html(rendered);

                // $('#response_div').empty()
            });
        })


    $('.create_portfolio').on('click','#create_link', function(event){ 
            event.preventDefault(); 
            $('.update_class_form').load("/portfolio/create");
        })

    $('body').on('click','.view_dash_portfolio', function(event){
        event.preventDefault();
        $('.tab-content').load("/portfolio/portfolio_detail/"+$(this).data("portfolio_id"));
    })

getPortfolios();
$('.update_class_form').on('submit', '#update_form',function(event){
        event.preventDefault();
        var action = $(this).attr('action') ; 
        $.post(action, $(this).serialize(), function(data){
            console.log(data);
            $('.list_portfolios').empty()
            getPortfolios(data);
        });
    });

});
