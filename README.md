[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<br />
<p align="center">
  <a href="https://github.com/normangalt/Cosmetics-Check/repo_name">
    <img src="tg_bot_logo.jpg" alt="Logo" width="120" height="120">
  </a>

  <h3 align="center">MakeUpCheckUp</h3>

  <p align="center">
    The bot that helps to learn more about the ingredients in the cosmetic products you use.
    <br />
    <a href="https://github.com/normangalt/Cosmetics-Check"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/normangalt/Cosmetics-Check">View Demo</a>
    ·
    <a href="https://github.com/normangalt/Cosmetics-Check/issues">Report Bug</a>
    ·
    <a href="https://github.com/normangalt/Cosmetics-Check/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
      <ul>
        <li><a href="#Data">Data</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#credits">Credits</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project is designed to show information about cosmetics and how safe they are.
The program creates a telegram bot. To use it, user need to send the photo of the composition of ingredients of a cosmetics product. Then he/she receives data about the safety of those ingredients and (if one wants) additional information about them.

The self-care industry is expanding, there are many self-care products that billions of people use every day. However, there is lack of people who has enough knowledge in the field to understand how each component of the product can effect one's health. Manufacturers can use this defect and use the ingredients that are beneficial to business and not to human health.

Our aim is to make the using of cosmetic products as safe as possible by providing the service with an access to the inforamtion about the ingredients and protect the health of everyone who uses it.

To try it, find the @CosmeticsConsistensionBot in Telegram yourself.

### Data

In the project databases from the The Cosmetic Ingredient Review (https://cir-safety.org/about) are used.

The Cosmetic Ingredient Review was established in 1976 by the industry trade association (then the Cosmetic, Toiletry, and Fragrance Association, now the Personal Care Products Council), with the support of the U.S. Food and Drug Administration and the Consumer Federation of America. Although funded by the Council, CIR, the Expert Panel for Cosmetic Ingredient Safety, and the review process are independent from the Council and the cosmetics industry. CIR and the Expert Panel for Cosmetic Ingredient Safety operate under a set of procedures.

The prohibited be FDA ingedients are retrieved from the following database: https://www.cir-safety.org/supplementaldoc/prohibited/restricted-fda

The overall information about the ingredients is retrieved from the following database: https://cir-safety.org/sites/default/files/SQ-breakout-092020.pdf


### Built With

* [TelegramAPI](https://core.telegram.org)
* [GOOGLE-Cloud-Vision](https://cloud.google.com/vision)
* [Pandas](https://pandas.pydata.org)
* [OS](https://docs.python.org/3/library/os.path.html)


<!-- USAGE EXAMPLES -->
## Usage

To get the information about the ingredients of the cosmetic product, the user needs to send the command /sendphoto to the @CosmeticsConsistensionBot, the bot will answer that it is ready to take a photo. Then the user needs to send a photo of the composition of the product. With the google cloud vision, the program recognizes the text from the photo and checks if the are any prohibited ingredients among the components. If yes, the bot notifies the user. Then the bot asks if the user wants to know more about all the ingredients that were found in the composition. If the user clicks no, work with the photo ends. If the user clicks yes, the bot sends a conclusion on the ingredients from the CIR expert panel (https://cir-safety.org/about)and work with the photo is ends.

More detailed manual you will find in telegram bot.

See how the bot works in telegram. Go to the @CosmeticsConsistensionBot (https://t.me/CosmeticsConsistensionBot) and send a command /sendphoto

![image](https://user-images.githubusercontent.com/69758108/118395266-0016cd80-b652-11eb-8600-76270312a25d.png) ![image](https://user-images.githubusercontent.com/69758108/118395292-250b4080-b652-11eb-9455-1a9043c2d8c9.png)



## Roadmap

See the [open issues](https://github.com/normangalt/Cosmetics-Check/issues) for a list of proposed features (and known issues).



## License

Distributed under the MIT License. See `LICENSE` for more information.



## Feel free to contact

We are open to improvements in our project. If you have any ideas or you are ready to help, contact us!

Facebook: [Yaroslav_Brovchenko](https://www.facebook.com/profile.php?id=100007232269167)

Project Link: [https://github.com/normangalt/Cosmetics-Check](https://github.com/normangalt/Cosmetics-Check)



## Credits

* [firstgenius](https://github.com/firstgenius)
* [NormanGalt](https://github.com/normangalt)
* [S-Daria](https://github.com/S-Daria)
* [PHentosh](https://github.com/PHentosh)
* [Oleksandr](https://github.com/SashaRyha)





[contributors-shield]: https://img.shields.io/github/contributors/normangalt/Cosmetics-Check.svg?style=for-the-badge
[contributors-url]: https://github.com/normangalt/Cosmetics-Check/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/normangalt/Cosmetics-Check.svg?style=for-the-badge
[forks-url]: https://github.com/normangalt/Cosmetics-Check/network/members
[stars-shield]: https://img.shields.io/github/stars/normangalt/Cosmetics-Check.svg?style=for-the-badge
[stars-url]: https://github.com/normangalt/Cosmetics-Check/stargazers
[issues-shield]: https://img.shields.io/github/issues/normangalt/Cosmetics-Check.svg?style=for-the-badge
[issues-url]: https://github.com/normangalt/Cosmetics-Check/issues
[license-shield]: https://img.shields.io/github/license/normangalt/Cosmetics-Check.svg?style=for-the-badge
[license-url]: https://github.com/normangalt/Cosmetics-Check/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/yaroslav-brovchenko-247477205/
