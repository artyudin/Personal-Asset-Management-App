from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from portfolio.models import Portfolio
from users.models import Profile
from .analysis_models import Client, Risk, Investment_policy


def report(request):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Investment_policy.pdf"'

        buffer = BytesIO()

        # Create the PDF object, using the BytesIO object as its "file."
        p = canvas.Canvas(buffer)
        user = request.user
        client = Client.objects.get(user=user)
        investment = Investment_policy.objects.get(user=user)
        profile = Profile.objects.get(user=user)
        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        p.drawString(500,20,"PAM®")
        p.setTitle("Investment Policy")
        p.setFont("Helvetica-Bold", 24)
        p.drawCentredString(250, 800, "Investment Policy")


        

        p.setFont("Times-Roman", 12)
        gap = 20
        y = 780
        x = 400

        p.drawString(x,y,'Client Name: '+user.first_name +' '+user.last_name)
        p.drawString(x,y- gap * 1,'Email address: '+user.email)
        p.drawString(x,y- gap * 2,'Phone Number: '+profile.phone_number)
        
        
        gap = 30

        y = 700
        x = 300
        p.drawString(x,y,client.age)
        p.drawString(x,y- gap * 1,client.marital_status)
        p.drawString(x,y- gap * 2,client.income)
        p.drawString(x,y- gap * 3,client.saving_rate)
        p.drawString(x,y- gap * 4,client.fixed_expenses)
        p.drawString(x,y- gap * 5,str(client.federal_tax))
        p.drawString(x,y- gap * 6,str(client.state_tax))
        x = 100
        p.drawString(x,y,"Age Range:")
        p.drawString(x,y- gap * 1,"Marital Status:")
        p.drawString(x,y- gap * 2,"Income Range:")
        p.drawString(x,y- gap * 3,"Saving Rate:")
        p.drawString(x,y- gap * 4,"Fixed Expenses:")
        p.drawString(x,y- gap * 5,"Federal Taxes:")
        p.drawString(x,y- gap * 6,"Staets Taxes:")

        y = 450
        x = 300
        p.drawString(x,y,investment.time_retirement)
        p.drawString(x,y- gap * 1,investment.liquidity_needs)
        p.drawString(x,y- gap * 2,investment.goal_short)
        p.drawString(x,y- gap * 3,investment.goal_mid)
        p.drawString(x,y- gap * 4,investment.goal_long)
        p.drawString(x,y- gap * 5,str(investment.expected_return))
        p.drawString(x,y- gap * 6,str(investment.expected_inflation))
        x = 100
        p.drawString(x,y,"Time before retirement:")
        p.drawString(x,y- gap * 1,"Need to liquidity:")
        p.drawString(x,y- gap * 2,"Short Goal:")
        p.drawString(x,y- gap * 3,"Mid Goal:")
        p.drawString(x,y- gap * 4,"Long Goal:")
        p.drawString(x,y- gap * 5,"Expected Return:")
        p.drawString(x,y- gap * 6,"Expected Inflation:")




        # Close the PDF object cleanly.
        p.showPage()
        p.save()

        # Get the value of the BytesIO buffer and write it to the response.
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response