# portfolio

Module 10


Create a Portfolio
There are two options for creating a portfolio:

Customize a template to show off your work. Include images, links to GitHub repos, and contact information (LinkedIn profile, email address, etc.).
Make sure the portfolio is easily viewed on phones, tablets, and computers.

A portfolio is a tool used to showcase your talents. When a clean, clear, and well-organized portfolio is included with a resume, it makes an impression. Robin is well aware that to become an employee of NASA, she needs to market herself to her best ability, and that includes creating a portfolio.

Creating one from a blank slate is a little daunting, so it's a good idea to use a template when available. Click the following link to download the portfolio templates. Note that you will need to unzip the file to access the templates.

templates.zip (Links to an external site.)

Open one of the HTML files in your web browser and explore it. Note it has all the hallmarks of a good portfolio:

It's clean, with no distracting clutter.
It captures your projects with eye-catching images and quick summaries.
There are links to your presence everywhere—LinkedIn, GitHub, email, etc.
It's personable, and after adding your personal touch, it will be more so.
Feel free to use this or one of the other templates to start building a portfolio. Follow the prompts within the code to customize it with your own images and links. The basic portfolios here are a great start, but feel free to make adjustments or add your own flair. Fonts, colors, image sizes—there are few limitations on what you can do.

Customize the Portfolio
This portfolio template already links to Bootstrap 4.3.1, but it also has a custom stylesheet included. To change the background of the body, for example, navigate to that style sheet and add this line:

body {
   margin: 5px;
   padding-bottom: 70px;
   background-color: darkgray;
}
Save the stylesheet, then refresh your browser. Notice that the background is dark gray instead of white? Each element in your HTML can be adjusted this way.

Here are some tips to help with customizing:

Your featured images should be .png files generated from the project you're featuring, such as a graph made in Matplotlib, a visual you've created that represents the project, or an interesting screenshot of your work.

Sometimes the Bootstrap CSS customization needs to be overwritten. To ensure your stylesheet's code takes precedence, add !important; to the line of code you want changed, like in the code below.

body {
margin: 5px;
padding-bottom: 70px;
background-color: darkgray !important;
}
Images can be used as backgrounds. Just be careful that they don't distract from your featured projects.

Background images and colors aren't the only way to add personal touch—free fonts (such as Google Fonts (Links to an external site.)) are also great.

There are loads of great resources on CSS customization out on the web, too, for any other specific questions you may have.

Add Your Portfolio to GitHub
Your portfolio is something you'll want several other projects linked to. As such, it's best to keep it in its own repository.

From your GitHub homepage, create a new repository named "portfolio" and clone it into the master folder containing all of your class projects. Download one of the portfolio templates into this folder, then customize it to fit you-your personality, goals, and favorite projects.
