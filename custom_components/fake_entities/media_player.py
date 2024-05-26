from homeassistant.components.media_player import (
    MediaPlayerEntity,
    SUPPORT_PLAY,
    SUPPORT_PAUSE,
    SUPPORT_STOP,
    SUPPORT_PREVIOUS_TRACK,
    SUPPORT_NEXT_TRACK,
    SUPPORT_VOLUME_SET,
    SUPPORT_VOLUME_MUTE,
    SUPPORT_SELECT_SOURCE,
    SUPPORT_PLAY_MEDIA,
)

class Fakemedia_playerEntity(MediaPlayerEntity):
    """Representation of a fake media_player entity."""

    def __init__(self, name):
        """Initialize the media_player entity."""
        self._name = name
        self._volume_level = 1.0  # Default volume level
        self._is_muted = False  # Default mute status
        self._media_title = "Fake Media Title"  # Default media title
        self._media_artist = "Fake Media Artist"  # Default media artist
        self._source = "Fake Source"  # Default source
        self._source_list = ["Fake Source 1", "Fake Source 2"]  # Default source list
        self._state = "off"  # Default state

    @property
    def name(self):
        """Return the name of the media_player entity."""
        return self._name

    @property
    def volume_level(self):
        """Volume level of the media player (0..1)."""
        return self._volume_level

    @property
    def is_volume_muted(self):
        """Boolean if volume is currently muted."""
        return self._is_muted

    @property
    def media_title(self):
        """Title of current playing media."""
        return self._media_title

    @property
    def media_artist(self):
        """Artist of current playing media."""
        return self._media_artist

    @property
    def source(self):
        """Name of the current input source."""
        return self._source

    @property
    def source_list(self):
        """List of available input sources."""
        return self._source_list

    @property
    def state(self):
        """State of the player."""
        return self._state

    @property
    def supported_features(self):
        """Flag media player features that are supported."""
        return SUPPORT_PLAY | SUPPORT_PAUSE | SUPPORT_STOP | SUPPORT_PREVIOUS_TRACK | SUPPORT_NEXT_TRACK | SUPPORT_VOLUME_SET | SUPPORT_VOLUME_MUTE | SUPPORT_SELECT_SOURCE | SUPPORT_PLAY_MEDIA
async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the fake media_player entry."""
    async_add_entities([Fakemedia_playerEntity("Fake Media Player")])
    return True