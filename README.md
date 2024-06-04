<a name="readme-top"></a>
<br />
<div align="center">
  <a href="https://github.com/Fett-Mops/Game-Of-Live-SenseHat">
    <img src="logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Game of Live Sense HAT</h3>

  <p align="center">
   Simulating Conways game of life on the sense HAT add-on for the raspberrypi
   <br/>
   :warning:Has yet to be finished :warning:
    <br />
    <a href="https://github.com/Fett-Mops/Game-Of-Live-SenseHat">View Demo</a>
    ·
    <a href="https://github.com/Fett-Mops/Game-Of-Live-SenseHat/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/Fett-Mops/Game-Of-Live-SenseHat/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
     <a href="#usage">Usage</a>
        <li><a href="#menue">Menue</a></li>
    </li>
    <li><a href="#contributing">Contributing</a></li>


    +

  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/il.png" alt="HAT" width="80" height="80">
  </a>

This project is about a Game of Life Simulation with SenseHat on Raspberrypi. The more sensores i discovered on the modul the more i wanted to use so the menuing isnt very intuitive but i wanted to build in some of the sensores it had. Also i thougth it would be a good idea to start with learning to use multithreading but as you can see i couldnt go in verry deep.

<!-- GETTING STARTED -->
## Getting Started

Before you start you need to connect the [raspberry pi](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) to the internet and isnstall the [Sense HAT](https://www.raspberrypi.com/products/sense-hat/) module.

### Prerequisites

if you dont have git install it with this command
  ```
  sudo apt install git
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Fett-Mops/Game-Of-Live-SenseHat/
   ```
2. Install sense-hat
   ```sh
    sudo apt install sense-hat
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
heres how to run the programm
```sh
python3 GoL.py
```
by default the colors of the LED's are random but if you dont like that you can use a predefined color like this

```sh
python3 GoL.py blue
```
<div align = "center">
  
   red 🟥
   blue 🟦
   green 🟩
   yellow 🟨
   purple 🟪
   white ⬜
   orange 🟧
   brown 🟫
 </div>
 brown [101, 67, 33]
 yellow [255, 255, 0]
 purple [106, 13, 173]
 white [255, 255, 255]
 orange [247, 152, 29]
 
or if you wan to use your own color you can define the rgb values itself
```sh
python3 GoL.py 130 200 177
```
### Menue
<p align="right">(<a href="#readme-top">back to top</a>)</p>
#### secret
in the secrete i would have done a rick roll yet it is very hard to recognize without the audio on a 8x8 display (it plays the audio if your earphones ar connected) 
thats why i decidet to use the Bad Apple as an alternative. it is more recognizable because of the contrast( the whole video is black white). also i recomend to put a paper above the display because it blends the LED's thogether.
here if you want to use ("Never Gonna Give You Up")[https://www.youtube.com/watch?v=dQw4w9WgXcQ] by Rick Astley
```sh
python3 GoL.py Rick
```
else it will play (Bad Apple) form ZUN.

if there is someone who really wants to have there own video implemented write an issue or contact me in another way. i know how to implement that but i didnt fellt the need because i already have all the options i could wish for :)






<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>
