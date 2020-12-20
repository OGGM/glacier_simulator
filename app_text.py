'''
the app text is structured in seven dictionaries:

header_text
    containing the help text and the headings for the buttons in the heading

panel_text
    containing the content of all panels, including: the select options, the heading of the widgets and the descriptions shown in the panels

tab_menu_headings
    containing the headings of the panels displayed in the tabs

geometry_plot_labels
    containing all the text displayed in the geometry plot

timeseries_plot_labels
    containing all the text displayed in the timeseries plots

timeseries_table_labels
    containing all the text of the timeseries table

figure_tab_headings
    containing the headings of the tabs of the figures
'''

supported_languages = ['en', 'de']

# text for app header, including help text
header_text = {
    # start page
    'help_start_page':
        {
            'en': ('<div style="font-size:20px">OGGM-Edu glacier simulator</div>' +
                   '<p style="margin-top: 0px;">' +
                   'With this app you can simulate idealized glaciers using the ' +
                   '<a href="https://oggm.org">OGGM</a> model. If you are not ' +
                   'familiar with the app yet, click "next" to go through the ' +
                   'instructions or go to the "find help here" section to ' +
                   'jump to a chosen chapter of the help. <br>This app was realised ' +
                   'with the <a href="https://holoviz.org">HoloViz</a> python packages.' +
                   '</p>'),
            'de': ('<div style="font-size:20px">OGGM-Edu Gletschersimulator</div>' +
                   '<p style="margin-top: 0px;">' +
                   'Mit dieser App können idealisierte Gletscher mithilfe des ' +
                   '<a href="https://oggm.org">OGGM</a> Models simuliert werden. ' +
                   'Wenn du das erstemal hier bist kannst du auf "weiter" drücken ' +
                   'und dir wird eine Beschreibung in der Kopfzeile angezeigt. Um ' +
                   'zwischen den Kapiteln der Hilfe zu springen schau unter ' +
                   '"Hilfe hier".<br>Diese App wurde mit tools von ' +
                   '<a href="https://holoviz.org">HoloViz</a> realisiert.' +
                   '</p>')
        },

    # beginner mode help
    'help_beginner_mode':
        {
            'en': ('<div style="font-size:18px">Beginner mode</div>' +
                   '<p style="margin-top: 0px;">' +
                   'In "beginner mode" (the default), you can change four model parameters: ' +
                   'the slope and the width profile of the glacier bed, the ELA ' +
                   '(Equilibrium Line Altitude) and the gradient of the mass-balance profile.' +
                   'Changes are becoming visible in the figures only after the ' +
                   '"run the model" button is clicked. In "beginner mode", the ' +
                   'model will always start from zero and will run until it reaches ' +
                   'equilibrium (volume approximately constant for 10 years).' +
                   '</p>'),
            'de': ('<div style="font-size:18px">Anfänger</div>' +
                   '<p style="margin-top: 0px;">' +
                   'Hier können vier Parameter des Models verändert werden: die Hangneigung, ' +
                   'die Gletscherweite, die ELA (Gleichgewichtslinie) und der Gradient des ' +
                   'Massenbilanzprofils. Die Änderungen werden in den Darstellungen sichtbar ' +
                   'nachdem der "Model starten" Knopf gedrückt wird. Das Model startet ' +
                   'jedesmal von Null und läuft solange ' +
                   'bis ein Gleichgewicht erreicht wird (Volumen bleibt ungefähr konstant ' +
                   'für 10 Jahre).' +
                   '</p>')
        },

    # advanced mode help
    'help_advanced_mode_1':
        {
            'en': ('<div style="font-size:18px">Advanced mode (I of III)</div>' +
                   '<p style="margin-top: 0px;">' +
                   'The "Advanced mode" allows for more complex experiments. ' +
                   'First, lets have a look at the ' +
                   '"run the model" tab. Here you can change the ELA (equilibrium line ' +
                   'altitude), the gradient of the mass balance profile (can define a ' +
                   'different gradient below and above the ELA, or set equal), Glen\'s creep ' +
                   'parameter, and if sliding at the glacier bed should be accounted for.' +
                   '</p>'),
            'de': ('<div style="font-size:18px">Fortgeschritten (I von III)</div>' +
                   '<p style="margin-top: 0px;">' +
                   'Als erstes zum "Modellauf" tab. Hier können die ELA (Gleichgewichtslinie), ' +
                   'der Gradient des Massenbilanzprofils (es können unterschiedliche gradienten ' +
                   'unter und über der ELA definiert werden, oder beide gleich gesetzt werden), ' +
                   'der Glen\'s creep Parameter, das Gleiten am Gletscherbed (Ja/Nein).' +
                   '</p>')
        },

    'help_advanced_mode_2':
        {
            'en': ('<div style="font-size:18px">Advanced mode (II of III)</div>' +
                   '<p style="margin-top: 0px;">' +
                   'In "Advanced mode", the model always continues from the current ' +
                   'glacier state. The slider "Years to advance model" defines for how ' +
                   'long the model should be running when clicking "advance model". ' +
                   'With "run to equilibrium", the model will ignore the slider and run ' +
                   'until equilibrium is reached.' +
                   '</p>'),
            'de': ('<div style="font-size:18px">Fortgeschritten (II von III)</div>' +
                   '<p style="margin-top: 0px;">' +
                   'In diesem Modus startet der Modellauf immer vom aktuellen Modelstand.'
                   'Mit "Jahre für Modellauf" wird definiert wielange das Model mit "Model ' +
                   'starten" laufen soll. Mit "bis zum Gleichgewicht" wird der Regler ' +
                   '"Jahre für Modelllauf" ignoriert und das Model läuft bis zum ' +
                   'Gleichgewicht.' +
                   '</p>')
        },

    'help_advanced_mode_3':
        {
            'en': ('<div style="font-size:18px">Advanced mode (III of III)</div>' +
                   '<p style="margin-top: 0px;">' +
                   'Now looking at the "create new model" tab. Here you can start with a ' +
                   'fresh glacier state by defining the width and the bedrock profile. If the linear profile is ' +
                   'selected, you can also choose its slope. By ' +
                   'clicking the "create new model" button the changes are getting visible ' +
                   'in the figures and a fresh glacier state is initialised.'
                   '</p>'),
            'de': ('<div style="font-size:18px">Fortgeschritten (III von III)</div>' +
                   '<p style="margin-top: 0px;">' +
                   'Jetzt zum "neues Model" tab. Hier kann ein neues Model von Null ' +
                   'gestartet werden. Dafür kann das Untergrundprofil, die ' +
                   'Gletscherweite und die Hangneigung (wenn das Untergrundprofil ' +
                   'linear gewählt wurde) gewählt werden. Mit einem Klick auf ' +
                   '"neues Model" werden die Änderungen wirksam und im ' +
                   'Diagramm angezeigt.'
                   '</p>')
        },

    # help page for geometry options
    'help_geometry_opt_1':
        {
            'en': ('<div style="font-size:18px">Geometry plots options (I of II)</div>' +
                   '<p style="margin-top: 0px;">' +
                   'Here you can change the bin width of the mass balance plot (top right). ' +
                   'You can also decide to display additional variables on the plots: ' +
                   'In the top left figure the ice velocity (red colormap), and in the bottom left figure ' +
                   'the ice thickness (blue colormap). The colorbars update their ' +
                   'upper limit according to the ' +
                   'current maximum values (shown in info text on the bottom right). ' +

                   '</p>'),
            'de': ('<div style="font-size:18px">Geometrie optionen (I von II)</div>' +
                   '<p style="margin-top: 0px;">' +
                   'Hier kann die Breite der Kästcehn im Massebilanz plot geänder werden (oben rechts). '
                   'Außerdem können zusätzlich Farbschatierungen in der "Geometrie Darstellung" ' +
                   'an- bzw. ausgeschaltet werden. Links oben kann die Eisgeschwindigkeit in rot' +
                   'und links unten die Eisdicke in blau angezeigt werden. Die Farbsakalen ' +
                   'sind dynamisch, das heißt das Maximum bezieht sich ' +
                   'auf die jeweiligen Maximalwerte welche im info text (rechts unten) ' +
                   'gezeigt werden.' +
                   '</p>')
        },

    'help_geometry_opt_2':
        {
            'en': ('<div style="font-size:18px">Geometry plots options (II of II)</div>' +
                   '<p style="margin-top: 0px;">' +
                   'The additional variable displays can be switched on after or before a model run. ' +
                   'When the colors are switched on for a model run, the calculation ' +
                   'takes much longer: this is why they are switched off per default. ' +
                   'To save calculation time you can switch off the update of the plots during the run. ' +
                   'You can also change the figure size and the text fontsize, ' +
                   'which can be useful to adapt to various screen sizes. ' +
                   'Note that you can also change the size of the whole app in ' +
                   'the browser window by pressing the "Strg" key and "+/-" or mouse scroll.' +
                   '</p>'),
            'de': ('<div style="font-size:18px">Geometrie optionen (II von II)</div>' +
                   '<p style="margin-top: 0px;">' +
                   'Die Farben können vor oder nach einem Modellauf ' +
                   'angezeigt werden. Modelläufe mit eingeschaltenen Farben benötigen ' +
                   'allerdings eine längere Rechenzeit. ' +
                   'Für einen schnelleren Modellauf kann das Updaten der Darstellung ausgeschaltet werden. ' +
                   'Mit "Darstellungsgröße skalieren" kann die Darstellungsgröße der oberen Reihe ' +
                   'der "Geometrie Darstellung" geändert werden, damit man nicht scrollen muss um ' +
                   'alle Bilder zu sehen. Mit "Schriftgröße Infotext" kann die Schriftgöße in der ' +
                   '"Geometrie Darstellung" angepasst werden, damit alle Informationen gelesen ' +
                   'werden können. Zusätzlich kann die Größe der app mit der "Strf" Taste und den ' +
                   'Tasten "+/-" im Browser verstellt werden.' +
                   '</p>')
        },

    # help page for timeseries options
    'help_timeseries_opt':
        {
            'en': ('<div style="font-size:18px">Timeseries plots options</div>' +
                   '<p style="margin-top: 0px;">' +
                   'Here you can choose which variables should be shown in the timeseries ' +
                   'plots.'
                   '</p>'),
            'de': ('<div style="font-size:18px">Zeitreihen optionen</div>' +
                   '<p style="margin-top: 0px;">' +
                   'Hier können die Parameter ausgewählt werden welche in den drei Zeitreihen ' +
                   'Bildern zu sehen sind.' +
                   '</p>')
        },

    # help page for model options
    'help_model_opt_1':
        {
            'en': ('<div style="font-size:18px">Model options (I of II)</div>' +
                   '<p style="margin-top: 0px;">' +
                   'In this section you can decide if the model should stop if the glacier is growing ' +
                   'outside the domain. There is also a option to toggle the buttons: i.e. ' +
                   'no second run can be started as long as the model is running.' +
                   '</p>'),
            'de': ('<div style="font-size:18px">Model optionen (I von II)</div>' +
                   '<p style="margin-top: 0px;">' +
                   'Es kann festgelegt werden, dass ein Modellauf abgebrochen wird wenn der ' +
                   'Gletscher die Domäne verlässt. Außerdem kann man entscheiden ob die Knöpfe ' +
                   'inaktive werden während eines Modellaufs und so verhindert werden, dass ' +
                   'ein zweiter Lauf gestartet ist während der vorherige noch aktiv ist.' +
                   'Mit dem Knopf "Buttons umschalten" können diese auch manuel umgeschaltet werden.' +
                   '</p>')
        },

    'help_model_opt_2':
        {
            'en': ('<div style="font-size:18px">Model options (II of II)</div>' +
                   '<p style="margin-top: 0px;">' +
                   'Moreover ' +
                   'you can define how often the current model state should be ' +
                   'shown in the plots ("show model progress every ... years") and you can ' +
                   'define a upper limit of calculation years when the model runs to equilibrium ' +
                   '("maximum calculation year of model"). This is useful to avoid idle states. All ' +
                   'changes are taken into account at the start of a model run. ' +
                   '</p>'),
            'de': ('<div style="font-size:18px">Model optionen (II von II)</div>' +
                   '<p style="margin-top: 0px;">' +
                   'Außerdem ' +
                   'kann definiert werden wieoft der Modelstatus während dem Modellauf ' +
                   'angezeigt werden soll ("zeige Modelfortschritt alle ... Jahre") und ' +
                   'es kann eine obere Grenze für einen Modellauf festgelegt werden ' +
                   '("Maximale Laufzeit eines Modellaufs (Jahre)"). Die Änderungen werden ' +
                   'mit jedem neuen Modellauf wirksam.' +
                   '</p>')
        },

    # help page for help panel
    'help_find_help_here':
        {
            'en': ('<div style="font-size:18px">Find help here</div>' +
                   '<p style="margin-top: 0px;">' +
                   'With the buttons you can jump directly to one of the help pages you want ' +
                   'to know more about. (Also to this page here ;)'
                   '</p>'),
            'de': ('<div style="font-size:18px">Hilfe hier</div>' +
                   '<p style="margin-top: 0px;">' +
                   'Mit den Knöpfen gelangt man direkt zu einzelnen Kapiteln der Hilfe. ' +
                   '(Auch zu dieser Seite hier ;).)'
                   '</p>')
        },

    # help for geometry plot
    'help_geometry_plot_1':
        {
            'en': ('<div style="font-size:18px">Glacier geometry plots (I of III)</div>' +
                   '<p style="margin-top: 0px;">' +
                   'The top left figure shows the glacier surface (dark blue) and its bed (grey) seen from the side. ' +
                   'The bottom left figure shows the glacier seen from above. ' +
                   'In both figures the blue line indicates the current glacier ' +
                   'state (in "advanced mode": the previous state is also ' +
                   'shown with a dashed line).' +
                   '</p>'),
            'de': ('<div style="font-size:18px">Geometrie Darstellung (I von III)</div>' +
                   '<p style="margin-top: 0px;">' +
                   'Das Bild oben links zeigt das Gletscherbettprofil von der Seite in grau. ' +
                   'Darunter ist das Getscherbett von oben gezeigt (Gletscherweite), die ' +
                   'dunkelgrauen Flächen bilden die Grenze. In beiden Bildern wird der aktuelle ' +
                   'Gletscherstand als weiße Fläche mit blauem Rand dargestellt. Wenn man das ' +
                   'Model mit "Fortgeschritten" betreibt, wird auch der letzte Gletscherstand ' +
                   '(Start des aktuellen Modellaufes) mit einer strichlieren Linie angezeigt.'
                   '</p>')
        },

    'help_geometry_plot_2':
        {
            'en': ('<div style="font-size:18px">Glacier geometry plots (II of III)</div>' +
                   '<p style="margin-top: 0px;">' +
                   'The top right figure shows the height dependent annual mass ' +
                   'balance as a black solid line (values on the upper x-axis). The horizontal dashed ' +
                   'line shows the equilibrium line altitude (ELA, which is also shown in ' +
                   'the figures on the left). The blue color is indicating a positive ' +
                   'mass balance (mass gain) and the red color is indicating a negative mass ' +
                   'balance (mass loss). Each elevation contributes to the glacier wide mass balance: ' +
                   'the relative contribution of each elevation bin can be seen on the colorbar to the ' +
                   "right of the figure. The length of the bar shows the elevation bin's area (x-axis)." +
                   '</p>'),
            'de': ('<div style="font-size:18px">Geometrie Darstellung (II von III)</div>' +
                   '<p style="margin-top: 0px;">' +
                   'Das Bild rechts oben zeigt die höhenabhängige jährliche Massenbilanz ' +
                   'als schwarze Linie. Die strichlierte Linie zeigt die Höhe der ELA an ' +
                   '(auch in den anderen zwei Bildern zu sehen). Blau steht dabei für eine positive ' +
                   'Massenbilanz (Massen gewinn) und rot für eine negative Massenbilanz (Massen ' +
                   'verlust). Die Schattierungen zeigen dabei den Beitrag zur gletscherweiten ' +
                   'Bilanz an und werden in der Farbskala angezeigt. Die Länge der Kästen zeigt ' +
                   'die Fläche eines Höhenbandes.' +
                   '</p>')
        },

    'help_geometry_plot_3':
        {
            'en': ('<div style="font-size:18px">Glacier geometry plots (III of III)</div>' +
                   '<p style="margin-top: 0px;">' +
                   'The text on the bottom right shows statistics of the current modelled glacier state. ' +
                   'AAR is the Accumulation Area Ratio, which describes the ratio of the accumulation area ' +
                   '(area above ELA) to the total area.' +
                   '<br>If you want to zoom into a figure, you can do this by clicking and drawing a rectangle in one of the figures. All other figures ' +
                   'will rezoom automatically to the same extent. To go back to the ' +
                   'original extent, click on the "Reset" button to the right of the ' +
                   'figures (two arrows forming a circle).' +
                   '</p>'),
            'de': ('<div style="font-size:18px">Geometrie Darstellung (III von III)</div>' +
                   '<p style="margin-top: 0px;">' +
                   'Der Text unten rechts zeigt aktuelle Werte des Models an. ' +
                   'AAR ist dabei die Accumulation Area Ratio, welche das Verhältnis der accumulations Fläche ' +
                   '(Fläche über ELA) zur gesamt Fläche beschreibt.' +
                   '<br>Wenn du hineinzoomen möchtest kannst du mit der Maus ein Rechteck ' +
                   'aufziehen (linke Maustaste gedrückt halten). Alle Bilder zoomen ' +
                   'automatisch auf den gleichen Ausschnitt. Um den Zoom rückgängig ' +
                   'zu machen auf "Reset" rechts neben den Bildern drücken (zwei ' +
                   'Pfeile welche einen Kreis formen).' +
                   '</p>')
        },

    # help page for timeseries plot
    'help_timeseries_plot_1':
        {
            'en': ('<div style="font-size:18px">Timeseries plots (I of II)</div>' +
                   '<p style="margin-top: 0px;">' +
                   'The three figures show the evolution of some glacier variables ' +
                   'with time. The resolution of the figures (how ' +
                   'often the state is shown) depends on the model settings (see ' +
                   '"model options"). After a model run has finished, the glacier state ' +
                   'gets a number and some model variable are shown ' +
                   'in the table at the bottom. The figures and the table are cleared ' +
                   'when a new glacier is initialized (e.g. after changing the bed or in beginner mode).' +
                   '</p>'),
            'de': ('<div style="font-size:18px">Zeitreihen Darstellung (I von II)</div>' +
                   '<p style="margin-top: 0px;">' +
                   'Die drei Bilder rechts zeigen die zeitlichen Verläufe unterschiedlicher ' +
                   'Gletscher Parameter (siehe Zeitreihen opt.). Die Auflösung hängt dabei ' +
                   'von den aktuellen Modeleinstellungen ab ' +
                   '(siehe "Modeloptionen"). Wenn ein Modellauf beendet wurde bekommt der ' +
                   'Abschnitt eine Nummer und es werden Modeleinstellungen in der Tabelle ' +
                   'angezeigt. Die Bilder und die Tabelle ' +
                   'werden gelöscht wenn ein neues Model gestartet wird.'
                   '</p>')
        },

    'help_timeseries_plot_2':
        {
            'en': ('<div style="font-size:18px">Timeseries plots (II of II)</div>' +
                   '<p style="margin-top: 0px;">' +
                   'You can zoom in and out on the plots by using the mousewheel ' +
                   'and you can use a mouseclick to drag the plots around. If you ' +
                   'zoom in on one plot the other plots will automatically rezoom ' +
                   'to the same time span. When moving with the mouse over the curves ' +
                   'a hover will show you the exact values of the points. To go back ' +
                   'to the original extent click on the "Reset" button to the right of ' +
                   'the figures (two arrows forming a circle).'
                   '</p>'),
            'de': ('<div style="font-size:18px">Zeitreihen Darstellung (II von II)</div>' +
                   '<p style="margin-top: 0px;">' +
                   'Mit dem Mausrad kann in die Bilder hineingezoomt werden und mit einem ' +
                   'Mausklick kann der Bildausschnitt verschoben werden. Alle Änderungen ' +
                   'des Bildausschnitts werden automatisch auf den anderen Bildern ' +
                   'aktualisiert. Mit "Reset" (zwei Pfeile welche einen Kreis formen) ' +
                   'rechts von den Bildern kann der Zoom rückgängig gemacht werden. ' +
                   'Wenn man mit dem Mauszeiger über die Kurven fährt ' +
                   'werden die genauen Werte der Zeitschritte angezeigt.'
                   '</p>')
        },

    # label for next button
    'next_button_text':
        {
            'en': 'Next',
            'de': 'Weiter'
        },

    # label for previous button
    'previous_button_text':
        {
            'en': 'Previous',
            'de': 'Zurück'
        },
}

# text for panels and their widgets
panel_text = {
    # beginner mode and advanced mode panels

    # options for bedrock profil, do not change order, first entry is default
    'bed_rock_profil_values':
        {
            'en': ['Linear', 'Getting flatter', 'Getting steeper', 'Cliff'],
            'de': ['Linear', 'Flächer werdend', 'Steiler werdend', 'Klippe']
        },

    # options for bedrock width, do not change order, first entry is default
    'bed_rock_width_values':
        {
            'en': ['Constant', 'Getting narrower', 'Getting wider',
                   'Wide top, narrow bottom'],
            'de': ['Konstant', 'Enger werden', 'Breiter werden',
                   'Oben weit, unten eng']
        },

    # options for glens creep parameter, do not change order, second entry is default
    'glens_creep_parameter_values':
        {
            'en': ['Small', 'Normal', 'Large'],
            'de': ['Klein', 'Normal', 'Groß']
        },

    # options for sliding, do not change order, first entry is default
    'sliding_parameter_values':
        {
            'en': ['No sliding', 'Sliding'],
            'de': ['Kein Gleiten', 'Gleiten']
        },

    # names for select widgets
    'bed_rock_slope_beginner_heading':
        {
            'en': 'Slope of bedrock profile',
            'de': 'Hangneigung'
        },

    'bed_rock_slope_advanced_heading':
        {
            'en': 'Slope of linear bedrock profile',
            'de': 'Hangneigung (lineares Untergrundprofil)'
        },

    'bed_rock_width_heading':
        {
            'en': 'Width along glacier',
            'de': 'Gletscherweite'
        },

    'mb_gradient_heading':
        {
            'en': 'Mass-Balance gradient (MB grad)',
            'de': 'Massenbilanzgradient (MB grad)'
        },

    'mb_gradient_below_heading':
        {
            'en': 'MB grad below ELA',
            'de': 'MB grad unter ELA'
        },

    'mb_gradient_above_heading':
        {
            'en': 'MB grad above ELA',
            'de': 'MB grad über ELA'
        },

    'mb_gradient_above_equal_below':
        {
            'en': ' equal below ELA',
            'de': ' gleich unter ELA'
        },

    'ELA_height_heading':
        {
            'en': 'ELA (equilibrium line altitude)',
            'de': 'ELA (Gleichgewichtslinie)'
        },

    'beginner_button_heading':
        {
            'en': 'Run the model',
            'de': 'Model starten'
        },

    'bed_rock_profil_heading':
        {
            'en': 'Bedrock profile',
            'de': 'Untergrundprofil'
        },

    'glens_creep_parameter_heading':
        {
            'en': "Glen's creep parameter",
            'de': "Glen's creep Parameter"
        },

    'sliding_parameter_heading':
        {
            'en': 'Sliding parameter',
            'de': 'Gleiten'
        },

    'years_to_advance_model_heading':
        {
            'en': 'Years to advance model',
            'de': 'Jahre für Modellauf'
        },

    'button_for_equilibrium_run_heading':
        {
            'en': 'Run to equilibrium',
            'de': 'Bis zum Gleichgewicht'
        },

    'button_to_advance_for_some_years_heading':
        {
            'en': 'Advance model',
            'de': 'Model starten'
        },

    'button_to_create_new_model_heading':
        {
            'en': 'Create new model',
            'de': 'Neues Model'
        },

    # headings for advanced mode tabs
    'run_model_tab_heading':
        {
            'en': 'Run the model',
            'de': 'Modellauf'
        },

    'create_new_model_tab_heading':
        {
            'en': 'Create new model',
            'de': 'Neues Model'
        },

    # geometry options panel

    'show_velocity_heading':
        {
            'en': 'Ice velocity (top left)',
            'de': 'Eisgeschwindigkeit (oben links)'
        },

    'show_thickness_heading':
        {
            'en': 'Ice thickness (bottom left)',
            'de': 'Eisdicke (unten links)'
        },

    'mb_curve_bin_width_heading':
        {
            'en': 'Min bin width of mb plot (top right)',
            'de': 'Min Bin Weite mb Plots (rechts oben)'
        },

    'geometry_figure_size_heading':
        {
            'en': 'Scale figure size',
            'de': 'Darstellungsgröße skalieren'
        },

    'geometry_figure_fontsize':
        {
            'en': 'Fontsize infotext',
            'de': 'Schriftgröße Infotext'
        },

    'show_geometry_plot_heading':
        {
            'en': 'Update geometry plots',
            'de': 'Update Geometrie Darstellung'
        },

    # timeseries opt panel

    'top_axis_heading':
        {
            'en': 'Top axis',
            'de': 'Obere Achse'
        },

    'middle_axis_heading':
        {
            'en': 'Middle axis',
            'de': 'Mittlere Achse'
        },

    'bottom_axis_heading':
        {
            'en': 'Bottom axis',
            'de': 'Untere Achse'
        },

    # options for timeseries plots, do not change order, first three entries are default
    'timeseries_axis_options':
        {
            'en': ['Volume', 'Area', 'Length','Max velocity',
                   'Max thickness', 'Max ice flux', 'Accumulation Area Ratio AAR'],
            'de': ['Volumen', 'Fläche', 'Länge', 'Max Geschwindigkeit',
                   'Max Dicke', 'Max Eisfluss', 'Accumulation Area Ratio AAR']
        },

    # panel for model options

    'stop_if_outside_heading':
        {
            'en': 'Stop run if glacier outside of domain',
            'de': 'Stop wenn Gletscher außerhalb'
        },

    'toggle_buttons_checkbox_heading':
        {
            'en': 'Toggle buttons during run',
            'de': 'Buttons umschalten während Modellauf'
        },

    'toggle_buttons_button_heading':
        {
            'en': 'Toggle buttons',
            'de': 'Buttons umschalten'
        },

    'dyears_model_slider_heading':
        {
            'en': 'Show model progress every .. years',
            'de': 'Zeige Modelfortschritt alle .. Jahre'
        },

    'max_calc_years_slider_heading':
        {
            'en': 'Abort model after .. years',
            'de': 'Model abbrechen nach .. Jahren'
        },

    # help panel

    'help_panel_description':
        {
            'en': ('<p style="margin-top: 0px;">Click on any button to get help on a given topic. ' +
                   'Navigate with the "Next" and "Previous" buttons on the top right.' +
                   '</p>'),
            'de': ('<p style="margin-top: 0px;">Auf Button drücken um Hilfe in der ' +
                   'Kopfzeile anzuzeigen. Navigieren mit dem "weiter" und ' +
                   '"zurück" Button (Kopfzeile rechts)')
        },
}

# headings of menu tabs
tab_menu_headings = {
    'beginner_mode':
        {
            'en': 'Beginner mode',
            'de': 'Anfänger'
        },

    'advanced_mode':
        {
            'en': 'Advanced mode',
            'de': 'Fortgeschritten'
        },

    'geometry_opt':
        {
            'en': 'Geometry opt.',
            'de': 'Geometrie opt.'
        },

    'timeseries_opt':
        {
            'en': 'Timeseries opt.',
            'de': 'Zeitreihen opt.'
        },

    'model_opt':
        {
            'en': 'Model opt.',
            'de': 'Model opt.'
        },

    'find_help_here':
        {
            'en': 'Find help here',
            'de': 'Hilfe hier'
        },

    'geometry_plot':
        {
            'en': 'Geometry plots',
            'de': 'Geometrie Darstellung'
        },

    'timeseries_plot':
        {
            'en': 'Timeseries plots',
            'de': 'Zeitreihen Darstellung'
        },
}

# labels for geometry plot
geometry_plot_labels = {
    'bedrock_x_label':
        {
            'en': 'Distance along glacier (km)',
            'de': 'Distanz entlang des Gletschers (km)'
        },

    'bedrock_height_y_label':
        {
            'en': 'Altitude (m)',
            'de': 'Höhe (m)'
        },

    'bedrock_width_y_label':
        {
            'en': 'Width (m)',
            'de': 'Weite (m)'
        },

    'glacier_label':
        {
            'en': 'Glacier',
            'de': 'Gletscher'
        },

    'mb_x_label':
        {
            'en': 'Annual Mass-Balance (mm w.e./year)',
            'de': 'Jährliche Massenbilanz (mm w.e/Jahr)'
        },

    'area_x_label':
        {
            'en': 'Bin area',
            'de': 'Bin Fläche'
        },

    'mb_label':
        {
            'en': 'Mass-Balance (MB)',
            'de': 'Massenbilanz (MB)'
        },

    'info_text_new_model':
        {
            'en': 'New Model geometry\ninitialised',
            'de': 'Neue Model Geometry\ninitialisiert'
        },

    'info_text_switched_off':
        {
            'en': 'This plot is currently not updated during the model run.\nTo switch it on go to "Geometry opt.".',
            'de': 'Dieses Diagramm wird aktuell nicht aktualisiert.\nAktivieren unter "Geometrie opt."'
        },

    'info_text_running_model':
        {
            'en': 'Model is running:',
            'de': 'Model läuft:'
        },

    'info_text_equilibrium':
        {
            'en': 'Model reached equilibrium',
            'de': 'Model beendet und im Gleichgewicht'
        },

    'info_text_stopped_model':
        {
            'en': 'Model finished',
            'de': 'Model beendet'
        },

    'info_text_aborted_model':
        {
            'en': 'Model stopped (max calculation time reached, see "Model opt.")',
            'de': 'Modellauf abgebrochen (maximale Zeit erreicht, siehe "Model opt.")'
        },

    'info_text_outside_domain':
        {
            'en': 'Model stopped (glacier outside of domain, see "Model opt.")',
            'de': 'Modellauf abgebrochen (Gletscher außerhalb der Domäne, siehe "Model opt.")'
        },

    'info_text_statistics':
        {
            'en': ('\nTime: {:4.0f} years     Length: {:4.2f} km      Area: {:.2f} km²     Volume: {:.2f} km³\n'
                   'Max ice thickness: {:.0f} m          Max ice velocity: {:.0f} m/year\n'
                   'AAR: {:.2}     Glacier-wide Mass-Balance: {:.2f} mm w.e./year'),
            'de': ('\nZeit: {:4.0f} years     Länge: {:4.2f} km      Fläche: {:.2f} km²     Volumen: {:.2f} km³\n'
                   'Max Eisdicke: {:.0f} m          Max Eisgeschwindigkeit: {:.0f} m/year\n'
                   'AAR: {:.2}     Gletscherweite Massenbilanz: {:.2f} mm w.e./year')
        },
}

# labels for timeseries plot
timeseries_plot_labels = {
    'x_label':
        {
            'en': 'Time (years)',
            'de': 'Zeit (Jahre)'
        },

    'y_label_volume':
        {
            'en': 'V (km³)',
            'de': 'V (km³)'
        },

    'y_label_area':
        {
            'en': 'A (km²)',
            'de': 'A (km²)'
        },

    'y_label_length':
        {
            'en': 'L (km)',
            'de': 'L (km)'
        },

    'y_label_max_velocity':
        {
            'en': 'u\u2098\u2090\u2093 (m/year)',
            'de': 'u\u2098\u2090\u2093 (m/Jahr)'
        },

    'y_label_max_thickness':
        {
            'en': u'h\u2098\u2090\u2093 (m)',
            'de': u'h\u2098\u2090\u2093 (m)'
        },

    'y_label_max_ice_flux':
        {
            'en': u'f\u2098\u2090\u2093 (m³/year)',
            'de': u'f\u2098\u2090\u2093 (m³/Jahr)'
        },
    'y_label_AAR':
        {
            'en': 'AAR',
            'de': 'AAR'
        },
}

# labels for timeseries table
timeseries_table_labels = {
    'table_heading_1':
        {
            'en': ['Profile', 'Slope (°)', 'Width (m)', 'ELA (m)',
                   'MB Gradient (mm w.e./year/m)', 'Glen\'s creep',
                   'Sliding', 'Years'],
            'de': ['Untergrundprofil', 'Hangneigung (°)', 'Gletscherweite',
                   'ELA (m)', 'Gradient (mm w.e./Jahr/m)',
                   'Glen\'s creep', 'Gleiten', 'Jahre']
        },

    'table_heading_2':
        {
            'en': ['In equilibrium', 'Outside domain'],
            'de': ['Im Gleichgewicht', 'Außerhalb der Domäne']
        },

    'yes_label':
        {
            'en': 'Yes',
            'de': 'Ja'
        },

    'no_label':
        {
            'en': 'No',
            'de': 'Nein'
        },
}

# headings for figure tab
figure_tab_headings = {
    'geometry_plot':
        {
            'en': 'Geometry plots',
            'de': 'Geometrie Darstellung'
        },

    'timeseries_plot':
        {
            'en': 'Timeseries plots',
            'de': 'Zeitreihen Darstellung'
        },
}
