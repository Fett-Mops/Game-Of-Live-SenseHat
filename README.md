<a name="readme-top"></a>
<br />
<div align="center">
  <a href="https://github.com/Fett-Mops/Game-Of-Live-SenseHat">
    <img src="img/logo.png" alt="Logo" width="80" height="80">
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
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

  <a >
    <img src="images/hat.png" alt="HAT" width="80" height="80">
  </a>

This project is about a Game of Life Simulation with SenseHat on Raspberrypi. The more sensores i discovered on the modul the more i wanted to use them and so i did. Also i thougth it would be a good idea to start with learning to use multithreading but as you can see i couldnt go in verry deep.

<!-- GETTING STARTED -->
## Getting Started

Before you start you need to connect the [raspberry pi](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) to the internet and install the [Sense HAT](https://www.raspberrypi.com/products/sense-hat/) module.

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
    pip install -r requirements 
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
heres how to run the programm
```sh
python3 GoL.py
```
by default the colors of the LED's are grey but if you dont like that you can use a predefined color like this

```sh
python3 GoL.py -b
```
<div align = "center">
  
   -r 🟥 
   -b 🟦
   -g 🟩 
   -y 🟨
   -p 🟪
   -w ⬜
   -o 🟧
   -b 🟫
   -gr ⬜
   -rand 🌈
 </div>

### Menue
ok so you start in the Home menue. if you shake the raspi hard it randamizes the hole grid. now you can press the joistick to start simulation. press again to pause. if you want to reset the grid put the raspi on his had wait a bit and all the leds should be dead. if you press long you can go to home mode here or in pause mode you can enter with up prebuild mode here you can choose between diffrent prebuild shapes to simulate. with right you enter custom gird mode where you can move a curser wich is blinking in red and inverts the pixel underneth if you push the joistick in. to leav this mode you have to hold in the middle the joistick to go in home mode again in wich you can with a simple push simulate your grid. if you push left or down you get to the secred noted below.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Secret
In the secrete i would have done a rick roll yet it is very hard to recognize without the audio on a 8x8 display (it plays the audio if your earphones are connected) 
thats why i decidet to use the Bad Apple as an alternative. it is more recognizable because of the contrast( the whole video is black&white). Also i recomend to put a paper above the display because it blends the LED's thogether.
here if you want to use ["Never Gonna Give You Up"](https://www.youtube.com/watch?v=dQw4w9WgXcQ) by Rick Astley you have to push the joistick down in the pause or home mode
but if you push left it will play ["Bad Apple"](https://www.youtube.com/watch?v=FtutLA63Cp8) form ZUN.

if there is someone who really wants to have there own video implemented write an issue or contact me in another way. I know how to implement that but i didnt fellt the need because i already have all the options i could wish for :) or you can do it yourself by modifying the code and convert a mp4 to frames via vid_to_frames.py.






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
