$(document).ready(function(){
        

        var asset_template = $('#asset-form-tmp').html();
        var template = $('#menu-tmp').html();
        var rendered = Mustache.render(template,{'form':asset_template});
        $('div.form-container').html(rendered);

        $('#bt1').on('click', function(event){ 
            $('.securities-container').empty();
            $.get('/securities/list_stock', function(data){
                $('#content-type').attr('value',data['content_type'])
                $('#choice').find('option').remove().end();
                $.each(data['stocks'], function (i, item) {
                    $('#choice').append($('<option>', { 
                        value: [item.symbol, item.id , item.company_name, item.sector, item.industry, item.market_capitalisation],
                        text : item.symbol
                    }));
                });

        })
            var stock = $('#choice>option:selected').val()
            console.log(stock);
        });



        $('#bt2').on('click', function(event){ 
            $('.securities-container').empty();
            $.get('/securities/list_bond', function(data){
                $('#content-type').attr('value',data['content_type']) 
                $('#choice').find('option').remove().end();
                $.each(data['bonds'], function (i, item) {
                    $('#choice').append($('<option>', { 
                        value: [item.symbol, item.id , item.company_name, item.coupon, item.maturity_date, item.sp_rating, item.moody_rating],
                        text : item.symbol
                    }));
                 
                });

            });
        });


        $('#bt3').on('click', function(event){ 
            $('.securities-container').empty();
            $.get('/securities/list_etf', function(data){
                $('#content-type').attr('value',data['content_type']) 
                $('#choice').find('option').remove().end();
                $.each(data['exchangeTradedFunds'], function (i, item) {
                    $('#choice').append($('<option>', { 
                        value: [item.symbol, item.id , item.name, item.category, item.fund_family, item.beta, item.alpha, item.r_squared, item.sharpe_ratio],
                        text : item.symbol
                    }));

                });

            });
        });
        
       $("#choice").change(function() {
        
            $('.securities-container').empty();
            var items = [];
            var res = $("#choice option:selected").val().split(" ");
            items.push('<br><div class="col-sm-6">');
            items.push('<table class="table" >');
            $.each(res, function(i, item) {
                items.push('<tr><td>' + item + '</tr><tr>');
                        });  // close each()
            items.push('</table>');
            items.push('</div>');
            $('.securities-container').append( items.join('') );

        }); 


        var $portfolio_id = $('#portfolio_id').val();
        var getAssets = function getAssets(port){
                $.get("/securities/list_asset/"+ port ,function(data){
                console.log(data);
                var template = $('#asset-tmp').html();
                var rendered = Mustache.render(template,data);
                $('div.asset-container').html(rendered);
          
            });
        }

        getAssets($portfolio_id);

        $('div.form-container').on('submit', '#add_asset',function(event){
            event.preventDefault();
            var action = "/securities/create" ; 
            $.post(action, $(this).serialize(), function(data){
               getAssets($portfolio_id); 
                });

        
         });


    $('div.asset-container').on('click','a',function(){
            event.preventDefault();
            var $target = $(this).parent('li');
            var symbol = $(this).data('content_object');
            console.log(symbol)
            var type_asset = $(this).data('content_type');

            if(type_asset==='stock'){
                var path = "/securities/stock_detail/"+ symbol;
                $.get(path, function(data){
                    var template = $('#stock-tmp').html();
                    var rendered = Mustache.render(template,data);
                    $('div.asset-info').html(rendered);
                    // $target.find('div.asset-info').html(rendered);
                   
                });
            } else if ( type_asset==='bond'){
                var path = "/securities/bond_detail/"+ symbol;
                $.get(path, function(data){
                    var template = $('#bond-tmp').html();
                    var rendered = Mustache.render(template,data);
                    $('div.asset-info').html(rendered);



                });

            } else {
                var path = "/securities/etf_detail/"+ symbol;
                $.get(path, function(data){
                    var template = $('#etf-tmp').html();
                    var rendered = Mustache.render(template,data);
                    $('div.asset-info').html(rendered);
                    
                });

            }
            

    })

    $('div.asset-container').on('click','#delete',function(){
        event.preventDefault();
        var id = $(this).data('id_asset')
        var path = "/securities/delete/"+ id;
                $.get(path, function(data){

                getAssets($portfolio_id);
                });


    });

    // var doc = new jsPDF();
    // var specialElementHandlers = {
    //     '.asset-container': function (element, renderer) {
    //         return true;
    //     }
    // };

    // $('#cmd').click(function () {
    //     doc.fromHTML($('.asset-container').html(), 15, 15, {
    //         'width': 170,
    //             'elementHandlers': specialElementHandlers
    //     });
    //     doc.save('sample-file.pdf');
    //     console.log(doc);
    // });


    $('body').on('click','.view_dash_analysis', function(event){
        event.preventDefault();
        $('.tab-content').load("/analysis/beta_analysis/"+$(this).data("portfolio_id"));
    })
    $('body').on('click','.view_dash_compare', function(event){
        event.preventDefault();
        $('.tab-content').load("/analysis/compare/"+$(this).data("portfolio_id"));
    })
    

});
