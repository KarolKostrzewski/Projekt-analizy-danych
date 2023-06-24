import io
import base64
import matplotlib
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from django.shortcuts import render
from .nba import pobierz_graczy, Nba, PostSeason

def home(request):
    return render(request, 'home.html')

def nba(request):
    x=pobierz_graczy()
    active_players_full_name = x[0]
    active_players_id = x[1]
    seasons_list = x[2]
    list_stats = x[3]
    player1 = request.POST.get('player1-choice')
    player2 = request.POST.get('player2-choice')
    player3 = request.POST.get('player3-choice')
    seasons_countback = request.POST.get('number-choice')
    choosen_stat = request.POST.get('stat-choice')
    chart_image = None
    nba_instance = None
    chart1 = None
    chart2 = None
    chart3 = None
    if request.method == 'POST' and 'generate-chart' in request.POST:
        
        matplotlib.use('Agg')
        # Tworzenie instancji klasy i generowanie danych o graczach
        nba_instance = Nba(player1, player2, player3,seasons_countback,choosen_stat,active_players_id)
        nba_instance.pobierz_dane()
        chart1 = nba_instance.pobierz_dane()[9]
        chart2 = nba_instance.pobierz_dane()[10]
        chart3 = nba_instance.pobierz_dane()[11]
        # Przygotowanie bufora do renderowania wykresu
        fig = Figure(figsize=(15, 7), dpi=80)
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)

        # Tworzenie wykresu liniowego
        ax.plot(nba_instance.selected_seasons, nba_instance.stat1, label=player1)
        ax.plot(nba_instance.selected_seasons[:len(nba_instance.stat2)], nba_instance.stat2, label=player2)
        ax.plot(nba_instance.selected_seasons[:len(nba_instance.stat3)], nba_instance.stat3, label=player3)

        # Konfiguracja wykresu
        ax.set_xlabel('Sezony', fontsize=15)
        ax.set_ylabel(f'{choosen_stat}', fontsize=15)
        ax.set_title(f'Porównanie statystyki "{choosen_stat}" graczy w wybranych sezonach', fontsize=20)
        ax.legend(fontsize=14)
        ax.tick_params(axis='x', labelsize=14)
        ax.tick_params(axis='y', labelsize=15)

        # Renderowanie wykresu do bufora
        canvas.draw()

        # Konwersja bufora na obraz
        buffer = io.BytesIO()
        canvas.print_png(buffer)
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

        # Generowanie ścieżki do obrazu
        chart_image = f"data:image/png;base64,{image_base64}"

    else:
        chart_image = None
        
    context = {
        'player1': player1,
        'player2': player2,
        'player3': player3,
        'seasons_list':seasons_list,
        'list_stats':list_stats,
        'seasons_countback':seasons_countback,
        'active_players_full_name': active_players_full_name,
        'active_players_id':active_players_id,
        'choosen_stat ': choosen_stat,
        'nba_instance':nba_instance,
        'chart_image': chart_image,
        'chart1':chart1,
        'chart2':chart2,
        'chart3':chart3,
        }

    if context['seasons_countback'] is None:
        context['seasons_countback'] = 0
    return render(request, 'nba.html', context)

def nba_postseason(request):
    x=pobierz_graczy()
    active_players_full_name = x[0]
    active_players_id = x[1]
    seasons_list = x[2]
    list_stats = x[3]
    player1 = request.POST.get('player1-choice')
    player2 = request.POST.get('player2-choice')
    player3 = request.POST.get('player3-choice')
    seasons_countback = request.POST.get('number-choice')
    choosen_stat = request.POST.get('stat-choice')
    chart_image = None
    nba_instance = None
    chart1 = None
    chart2 = None
    chart3 = None
    if request.method == 'POST' and 'generate-chart' in request.POST:
        
        matplotlib.use('Agg')
        # Tworzenie instancji klasy i generowanie wykresu
        nba_instance = PostSeason(player1, player2, player3,seasons_countback,choosen_stat,active_players_id)
        nba_instance.pobierz_dane()
        chart1 = nba_instance.pobierz_dane()[9]
        chart2 = nba_instance.pobierz_dane()[10]
        chart3 = nba_instance.pobierz_dane()[11]
        # Przygotowanie bufora do renderowania wykresu
        fig = Figure(figsize=(15, 7), dpi=80)
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)

        # Tworzenie wykresu liniowego
        ax.plot(nba_instance.selected_seasons, nba_instance.stat1, label=player1)
        ax.plot(nba_instance.selected_seasons[:len(nba_instance.stat2)], nba_instance.stat2, label=player2)
        ax.plot(nba_instance.selected_seasons[:len(nba_instance.stat3)], nba_instance.stat3, label=player3)

        # Konfiguracja wykresu
        ax.set_xlabel('Sezony', fontsize=15)
        ax.set_ylabel(f'{choosen_stat}', fontsize=15)
        ax.set_title(f'Porównanie statystyki "{choosen_stat}" graczy w wybranych sezonach', fontsize=20)
        ax.legend(fontsize=14)  # Zwiększenie rozmiaru czcionki w legendzie
        ax.tick_params(axis='x', labelsize=14)  # Zwiększenie rozmiaru czcionki etykiet osi X
        ax.tick_params(axis='y', labelsize=15)

        # Renderowanie wykresu do bufora
        canvas.draw()

        # Konwersja bufora na obraz
        buffer = io.BytesIO()
        canvas.print_png(buffer)
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

        # Generowanie ścieżki do obrazu
        chart_image = f"data:image/png;base64,{image_base64}"

    else:
        chart_image = None
    context = {
        'player1': player1,
        'player2': player2,
        'player3': player3,
        'seasons_list':seasons_list,
        'list_stats':list_stats,
        'seasons_countback':seasons_countback,
        'active_players_full_name': active_players_full_name,
        'active_players_id':active_players_id,
        'choosen_stat ': choosen_stat,
        'nba_instance':nba_instance,
        'chart_image': chart_image,
        'chart1':chart1,
        'chart2':chart2,
        'chart3':chart3,
        }

    if context['seasons_countback'] is None:
        context['seasons_countback'] = 0
    return render(request, 'post.html', context)