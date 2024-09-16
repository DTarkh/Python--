# დავალება 1.
#
# შექმენით მედია ფლეიერის აპლიკაცია. განსაზღვრეთ ინტერფეისები
# 1)დაკვრის,
# 2)პაუზის,
# 3)გაჩერების
# 4)გადახვევის
# 5)სწრაფი წინსვლის ფუნქციებისთვის.
# განახორციელეთ კლასები აუდიო პლეერისთვის, ვიდეო პლეერისთვის და
# სტრიმინგის პლეერისთვის. დარწმუნდით, რომ თითოეული მოთამაშე
# ახორციელებს მხოლოდ მის ფუნქციონალურ ინტერფეისებს. მაქსიმალურად
# გამოიყენეთ SOLID პრინციპები!!!


class MediaPlayer:

    def play(self):
        pass
    def stop(self):
        pass
    def pause(self):
        pass

    def rewind(self):
        pass

    def fast_forward(self):
        pass

class Audio_player(MediaPlayer):
    def save_audio(self):
        pass

class Video_player(MediaPlayer):
    def reduce_video_size(self):
        pass

class Streaming_player(MediaPlayer):
    def go_live(self):
        pass


player_one = Audio_player()
player_one.save_audio()

player_two = Video_player()
player_two.reduce_video_size()

player_three = Streaming_player()
player_three.go_live()