from __future__ import unicode_literals
import datetime
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django_countries.fields import CountryField
from choices import AUDIO_FORMAT_CHOICES, COMPUTER_CHOICES, GENDER_CHOICES, \
    MOSTLY_CHOICES, STYLE_CHOICES, YEAR_CHOICES, YESNO_CHOICES, \
    NUM_MILONGA_CHOICES


LENGTH_1 = 300
LENGTH_2 = 50
LENGTH_CHOICES = 100


@python_2_unicode_compatible
class DJ(models.Model):

    # Person Data -------------------------------------------------------------
    user = models.OneToOneField(User, on_delete=models.SET_NULL,
                                null=True, blank=False)

    namesort = models.CharField(_("Hidden namesort"),
                                max_length=LENGTH_2,
                                default='', blank=True)

    name = models.CharField(_("Name"),
                            max_length=LENGTH_2,
                            default='', blank=True)

    gender = models.CharField(_("Gender"),
                              max_length=LENGTH_CHOICES,
                              choices=GENDER_CHOICES,
                              default='', blank=True)

    country = CountryField(_("Country"),
                           default='', blank=True)

    province = models.CharField(_("Province"),
                                max_length=LENGTH_2,
                                default='', blank=True)

    since = models.IntegerField(_("Since"),
                                choices=YEAR_CHOICES,
                                default=datetime.datetime.now().year,
                                blank=True)

    number_of_milongas = models.IntegerField(_("Number of milongas"),
                                             choices=NUM_MILONGA_CHOICES,
                                             default=0, blank=True)

    email = models.EmailField(_("Email"),
                              max_length=LENGTH_1,
                              default='', blank=True)

    # useremail = models.EmailField(_("UserEmail"),
    #                               max_length=LENGTH_1,
    #                               default='', blank=True)

    website = models.URLField(_("Website"),
                              max_length=LENGTH_1,
                              default='', blank=True)

    # Music Data --------------------------------------------------------------
    style = models.CharField(_("Style"),
                             max_length=LENGTH_CHOICES,
                             choices=STYLE_CHOICES,
                             default='', blank=True)

    cortinas = models.CharField(_("Tandas and cortinas"),
                                max_length=LENGTH_CHOICES,
                                choices=YESNO_CHOICES,
                                default='', blank=True)

    audioformat = models.CharField(_("Main audio format"),
                                   max_length=LENGTH_CHOICES,
                                   choices=AUDIO_FORMAT_CHOICES,
                                   default='', blank=True)

    audioformat2 = models.CharField(_("Alternative audio format"),
                                    max_length=LENGTH_CHOICES,
                                    choices=AUDIO_FORMAT_CHOICES,
                                    default='', blank=True)

    sources = models.CharField(_("Sources"),
                               max_length=LENGTH_1,
                               default='', blank=True)

    favorites = models.CharField(_("Personal favorites, decades"),
                                 max_length=LENGTH_1,
                                 default='', blank=True)

    music_remark = models.CharField(_("Remarks"),
                                    max_length=LENGTH_1,
                                    default='', blank=True)

    # Tech Data ---------------------------------------------------------------
    computer = models.CharField(_("Computer"),
                                max_length=LENGTH_CHOICES,
                                choices=COMPUTER_CHOICES,
                                default='', blank=True)

    computermodel = models.CharField(_("Computer model"),
                                     max_length=LENGTH_1,
                                     default='', blank=True)

    player = models.CharField(_("Player"),
                              max_length=LENGTH_1,
                              default='', blank=True)

    audiointerface = models.CharField(_("AudioInterface/DAC"),
                                      max_length=LENGTH_1,
                                      default='', blank=True)

    soundprocessor = models.CharField(_("Soundprocessor"),
                                      max_length=LENGTH_1,
                                      default='', blank=True)

    other_equipment = models.CharField(_("Other equipment"),
                                       max_length=LENGTH_1,
                                       default='', blank=True)

    compression = models.CharField(_("Compression"),
                                   max_length=LENGTH_CHOICES,
                                   choices=MOSTLY_CHOICES,
                                   default='', blank=True)

    equalization = models.CharField(_("Equalization"),
                                    max_length=LENGTH_CHOICES,
                                    choices=MOSTLY_CHOICES,
                                    default='', blank=True)

    equipment_remark = models.CharField(_("Remarks"),
                                        max_length=LENGTH_1,
                                        default='', blank=True)

    # Tech Data backup --------------------------------------------------------
    backup_computer = models.CharField(_("Computer"),
                                       max_length=LENGTH_CHOICES,
                                       choices=COMPUTER_CHOICES,
                                       default='', blank=True)

    backup_computermodel = models.CharField(_("Computer model"),
                                            max_length=LENGTH_1,
                                            default='', blank=True)

    backup_player = models.CharField(_("Player"),
                                     max_length=LENGTH_1,
                                     default='', blank=True)

    backup_audiointerface = models.CharField(_("AudioInterface/DAC"),
                                             max_length=LENGTH_1,
                                             default='', blank=True)

    backup_soundprocessor = models.CharField(_("Soundprocessor"),
                                             max_length=LENGTH_1,
                                             default='', blank=True)

    backup_other_equipment = models.CharField(_("Other equipment"),
                                              max_length=LENGTH_1,
                                              default='', blank=True)

    def __str__(self):
        return self.name
