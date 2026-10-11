class Playlist {
  constructor(tracks) {
    this.tracks = tracks;
    this.totalSeconds = 0;
    for (const track of tracks) {
      this.totalSeconds += track.seconds;
    }
  }

  add(track) {
    this.tracks.push(track);
    this.totalSeconds += track.seconds;
  }

  remove(title) {
    const index = this.tracks.findIndex((track) => track.title === title);
    if (index === -1) {
      return;
    }
    this.totalSeconds -= this.tracks[index].seconds;
    this.tracks.splice(index, 1);
  }

  byLength() {
    return this.tracks.sort((a, b) => a.seconds - b.seconds);
  }

  duration() {
    const minutes = Math.floor(this.totalSeconds / 60);
    const seconds = String(this.totalSeconds % 60).padStart(2, '0');
    return `${minutes}:${seconds}`;
  }
}

module.exports = { Playlist };
