import pygame
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # Initialize game, settings and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings,screen)
    alien = Alien(ai_settings,screen)
    #Creating the object to store statistics
    stats = GameStats(ai_settings)
    #Make play button
    play_button = Button(ai_settings,screen,"Play")
    # object for scoreboard
    sb = Scoreboard(ai_settings,screen,stats)
    # Make a group to store bullets,aliens
    bullets = Group()
    aliens = Group()


    #Create a fleet of aliens.
    gf.create_fleet(ai_settings,screen,ship,aliens)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,
            aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets)
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,
            bullets,play_button)

run_game()
