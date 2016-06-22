class ability(object):
    def __init__(self, name, about):
        self.name = name
        self.about = about
    
    def activate(self, activatee):
        if activatee.faction.AI == False:
            print("%s activated for %s." % (self.name, activatee.name))
        activatee.ability_active = True
        try:
            activatee.ability_effect = activatee.ability_effect * activatee.ability_factor
        except TypeError:
            pass
    
    def deactivate(self, activatee):
        if activatee.faction.AI == False:
            print("%s deactivated for %s." % (self.name, activatee.name))
        activatee.ability_active = False
        try:
            activatee.ability_effect = activatee.ability_effect / activatee.ability_factor
        except TypeError:
            pass

about_charge = '''This ability gives the unit that
wields it a major attack bonus,
but lowers their defense value.'''

about_courage = '''This ability doubles the defense
value of the unit that uses it and
raises their moral to 100%.'''

about_fire_arrows = '''Fire arrows grant an attack bonus to
ranged units when they are using their
ranged weapons.'''

about_leadership = '''Leadership gives all units fighting
under the hero with leadership a bonus,
whether attacking or defending.'''

about_command = '''Command allows the player to command
allied units in the same territory.'''

about_vision = '''Vision allows the player to see all
moves made on the map for a turn turns.'''

about_silence = '''Silence allows the unit to move in
enemy territory unseen, unless they
attack, or the enemy uses vision.'''

about_rage = '''Rage increases both the attack value
and the defense value of the unit.'''

about_burglar = '''Burglar allows the unit to move onto an enemy territory
and, either conquer it like other units, or they can
obtain double the resources from the territory while
they occupy it.'''

about_black_breath = '''The Black Breath will allow the user to freeze
enemy heroes, incapacitating them for two
rounds.'''

about_invulnerability = '''Invulnerability mantains the strength of the unit,
so that they cannot lose any of their men.'''

about_fear = '''Fear reduces enemy moral by half.'''

about_accuracy = '''Adds a large bonus to ranged combat.'''

about_resources = '''Resources triples the income of the territory
that the unit is on.'''

about_dragon_fire = '''Dragon Fire is only available to fire drakes
and increases their attack by lots.'''

charge = ability('Charge', about_charge)
courage = ability('Courage', about_courage)
fire_arrows = ability('Fire arrows', about_fire_arrows)
leadership = ability('Leadership', about_leadership)
command = ability('Command', about_command)
vision = ability('Vision', about_vision)
silence = ability('Silence', about_silence)
rage = ability('Rage', about_rage)
burglar = ability('Burglar', about_burglar)
fear = ability('Fear', about_fear)
invulnerability = ability('Invulnerability', about_invulnerability)
accuracy = ability('Accuracy', about_accuracy)
resources = ability('Resources', about_resources)
black_breath = ability('Black Breath', about_black_breath)
dragon_fire = ability('Dragon Fire', about_dragon_fire)
