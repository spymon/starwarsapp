from models.settings import db
from models.user import User
from models.note import Note
from models.manufacturer import Manufacturer
from models.platingColor import PlatingColor
from models.sensorColor import SensorColor
from models.productLine import ProductLine
from models.model import Model
from models.degree import Degree
from models.affiliation import Affiliation
from models.armament import Armament
from models.character import Character
from models.homeworld import Homeworld
from models.masterApprentice import MasterApprentice
from models.species import Specie
from models.characterAffiliation import CharacterAffiliation
from models.characterArment import CharacterArmament
from models.CharacterCybernetic import CharacterCybernetic
from models.characterHomeworld import CharacterHomeworld
from models.characterEquipment import CharacterEquipment
from models.characterEra import CharacterEra
from models.classType import ClassType
from models.cybernetic import Cybernetic
from models.equipment import Equipment
from models.era import Era
from models.formerAffiliation import FormerAffiliation
from models.gender import Gender



db.create_all()
