const { Playlist } = require('./playlist');

function tracks() {
  return [
    { title: 'Blue Monday', seconds: 448 },
    { title: 'Heroes', seconds: 371 },
    { title: 'Song 2', seconds: 122 },
  ];
}

describe('Playlist', () => {
  test('reports total duration as minutes and seconds', () => {
    expect(new Playlist(tracks()).duration()).toBe('15:41');
  });

  test('pads single-digit seconds', () => {
    expect(new Playlist([{ title: 'Short', seconds: 65 }]).duration()).toBe('1:05');
  });

  test('includes added tracks in the duration', () => {
    const playlist = new Playlist(tracks());
    playlist.add({ title: 'Intro', seconds: 19 });
    expect(playlist.duration()).toBe('16:00');
  });

  test('excludes removed tracks from the duration', () => {
    const playlist = new Playlist(tracks());
    playlist.remove('Heroes');
    expect(playlist.duration()).toBe('9:30');
  });

  test('ignores removal of a track that is not there', () => {
    const playlist = new Playlist(tracks());
    playlist.remove('Wonderwall');
    expect(playlist.duration()).toBe('15:41');
  });

  test('lists tracks from shortest to longest', () => {
    const titles = new Playlist(tracks()).byLength().map((track) => track.title);
    expect(titles).toEqual(['Song 2', 'Heroes', 'Blue Monday']);
  });
});
