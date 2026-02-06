import os

FILE_NAME = "playlist.txt"

def load_songs():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def save_songs(songs):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for song in songs:
            f.write(song + "\n")

def main():
    songs = load_songs()
    current_index = 0
    is_playing = False  # Состояние: играет музыка или нет

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("--- MY PLAYLIST ---")
        
        if not songs:
            print("The playlist is empty.")
        else:
            for i, song in enumerate(songs):
                prefix = "=> " if i == current_index else "   "
                print(f"{prefix}{i+1}. {song}")
            
            # Визуализация статуса
            status = "PLAYING ▶️" if is_playing else "STOPPED ⏸️"
            print(f"\nStatus: {status}")
            print(f"Current song: {songs[current_index]}")

        print("\nCommands: [a] Add, [d] Delete, [n] Next, [p] Prev")
        print("          [l] Play, [s] Stop, [q] Quit")
        choice = input("Select an action: ").lower()

        if choice == 'a':
            new_song = input("Enter song title: ")
            if new_song:
                songs.append(new_song)
                save_songs(songs)
        
        elif choice == 'd':
            if songs:
                songs.pop(current_index)
                save_songs(songs)
                if current_index >= len(songs) and songs:
                    current_index = len(songs) - 1
                is_playing = False # Останавливаем, если удалили текущую песню
        
        elif choice == 'n':
            if songs:
                current_index = (current_index + 1) % len(songs)
                is_playing = True # Авто-плей при переключении
        
        elif choice == 'p':
            if songs:
                current_index = (current_index - 1) % len(songs)
                is_playing = True # Авто-плей при переключении
        
        elif choice == 'l': # Play (Listen)
            if songs:
                is_playing = True
        
        elif choice == 's': # Stop
            is_playing = False
        
        elif choice == 'q':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()