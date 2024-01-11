# IGOR: Intelligent GO Robot

IGOR is a project focused on bringing an AI-power coach, teacher, and opponent to the board game Go, which comes from the Japanese word igo, where IGOR gets its name.  

## Motivation
- This project follows in the footsteps of a Hackathon project I participated in a few years ago - a chess-playing robot that I affectionately named [Chester](https://github.com/Michael73MGD/light-blue). Chester was built, programmed, and presented in just 24 hours during a covid-era hackathon in 2021. 

- Go is believed to have been first played over 4,500 years ago in China, and despite its simple rules, it was one of the last board games to be 'conquered' by artifial intelligence; this was done by AlphaGo in 2016. 
- Given its historical significance to humans and AI alike, I believe that Go deserves an AI-powered robot with the crucial ability to interact with a physical game to properly teach human players the rules, strategies, and joys of playing Go. 


## Project Breakdown
IGOR involves several mechanical and programatic projects working in tandem. They are outlined here:

- IGOR the physical robot
    - IGOR is built on the frame of an old 3D printer, allowing 3-axis motion for monitoring and interacting with the game board
    - Stepper motors move IGOR's tool head around the game board where it's camera can get a view of every piece's location, and allows the electromagnetic claw to manipulate stones (game pieces)
    - Custom 3D-printed stones are arranged on a 9x9 game board with embedded 8x3mm magnets, which allow the electromagnet on the tool head to pick up, move, and discard stones
    - The [Raspberry Pi camera module](https://www.raspberrypi.com/products/camera-module-v2/) mounted on the toolhead allows IGOR to view the game board after each human interaction
    - This is connected to a [Raspberry Pi 4](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) which controls the stepper motors of the robot, analyzes images, and decides IGOR's moves
- IGOR the AI
    - IGOR is also large language model-powered artificial intelligence that can be interacted with using text-to-speech and speech-to-text
    - For this functionality, IGOR the physical robot's Raspberry Pi connects to a locally-run instance of Llama2
    - This AI can control the difficulty level during a match, setup practice scenarios, explain rules and strategies, and offer coaching and encouragement to users, all through voice inputs
- IGOR in its final form
    - Go is an incredibly popular board game, though its high skill ceiling and complicated strategies make it intimidating for new players
    - The goal of IGOR is to successfully introduce Go, explain the rules to new players through physical examples and scenarios, and train them to be a competent player faster than any preprogrammed app, website, or human could hope to achieve. 
    - We've brought superior AI to Go, it's time to upgrade coaches to match and get more people into this historic game

### Task list
- 3D printed 9x9 Go board with divets that allow reliable placement of stones
    - See `STLs/board/full_board_VX.stl`
    - Board was custom designed for this purpose, inlcuding lines between each stone location and rounded divets for them to reliably fall into
- Stones embedded with iron (for the electromaget to attract)
    - [Hex nuts](https://a.co/d/gF2kllP)
        - The hex nut needs to be ferromagnetic (iron/steel) so that it can be picked up and released by the electromagnet
        - 304 Stainless Steel would not work for this purpose, therefore the zinc-plated steel nuts were used
    - See `STLs/board/stone_M6_hole_VX.stl`
    - Stone was designed starting from an online model (`STLs/STL_sources.md`), resized, trimmed, and with a M6 nut-sized hole in it for the hex nut to be placed in
- 3D printed electromagnetic stone mover (5V)
    - Electromagnets:
        - [20x15mm 5V](https://www.aliexpress.us/item/2251832388745731.html?spm=a2g0o.productlist.main.5.27407c36e4VteU&algo_pvid=15f16463-5bf9-4efb-90dd-8b5989f0b145&algo_exp_id=15f16463-5bf9-4efb-90dd-8b5989f0b145-2&pdp_npi=4%40dis%21USD%211.70%211.19%21%21%211.70%21%21%402103226117002704286314718e21e3%2112000024164379351%21sea%21US%212673377647%21&curPageLogUid=9mks4d6E7IZy)
        - [10x10mm 6V (selected)](https://www.aliexpress.us/item/2251832637809479.html?spm=a2g0o.detail.0.0.34b53153CTKQpz&gps-id=pcDetailTopMoreOtherSeller&scm=1007.40050.362094.0&scm_id=1007.40050.362094.0&scm-url=1007.40050.362094.0&pvid=083fd9e9-f589-4a9c-b498-bd4fd91a01a6&_t=gps-id:pcDetailTopMoreOtherSeller,scm-url:1007.40050.362094.0,pvid:083fd9e9-f589-4a9c-b498-bd4fd91a01a6,tpp_buckets:668%232846%238112%231997&pdp_npi=4%40dis%21USD%212.50%211.97%21%21%212.50%21%21%402103011017002704501335673efcc1%2164932969706%21rec%21US%212673377647%21)
    - Microphone / speaker
        - Bluetooth speaker should suffice
- 3D printed camera mount
    - Requirements:
        - Needs to be easily mounted/dismounted
        - Fits Raspberry Pi camera V2.1
        - Needs a good view of the game board
    - Solution: `STLs/raspi/picase_dovetail.stl`, `dove19.6.stl`, `picamcap.stl`
        - The Pi case is modified to mount onto the aluminum extrusions on the top of my 3D printer, and provides a dovetail mount at the front for the camera to slide onto
        - The camera mount is modified to slot into the dovetail and provide an ideal view of the printer bed

- 3D printed stone hopper
    - Requirements:
        - Needs to allow automatic feeding of stones to the electromagnet
        - Gravity driven, mounted to the side of the unit
        - Electromagnet moves to a position above the next stone and lifts it up, allowing the next to fall into place
        - Magnets in the stones cannot interfere, need to store them side to side
    - Custom designed from scratch to match needs and fit custom game stones
        - `STLs/Hopper/hopper_VX.stl`
        - Mounting solution will likely attach to the right side x-axis 
- Python programming running on the Raspberry Pi
    - Stone moving controls
    - Image capture controls
    - Image analysis
    - Go AI (non LLM)
    - Speech to text
    - Text to speech
- LLM run on a desktop
    - API connection to Raspberry Pi for sending/receiving LLM instructions
    - Ability to control Go AI difficulty
    - Ability to run a tutorial session
    - Ability to set up and explain practice scenarios
    - Stretch goals:
        - AI image generator - possibly pixel graphics. Generate an avatar for each difficulty, can regenerate each time
        - After every move, assess situation and generate an image along with a text response 
        - Model after a pixel graphics game with speech bubbles 