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
            'en': ('<div style="font-size:20px">OGGM edu glacier simulator</div>' +
                   '<p style="margin-top: 0px;">' +
                   'With this app you can simulate idealized glaciers using the ' +
                   '<a href="https://oggm.org">OGGM</a> model. If you are not ' +
                   'familiar with the app click on "next" to go through the ' +
                   'instruction or go to the "find help here" section to ' +
                   'jump to a certain chapter of the help. <br>This app was realised ' +
                   'using tools of <a href="https://holoviz.org">HoloViz</a>.' +
                   '</p>'),
            'de': ('<div style="font-size:20px">OGGM edu Gletschersimulator</div>' +
                   '<p style="margin-top: 0px;">' +
                   'Mit dieser App können idealisierte Gletscher mithilfe des ' +
                   '<a href="https://oggm.org">OGGM</a> Models simuliert werden. ' +
                   'Wenn du das erstemal hier bist kannst du auf "weiter" drücken ' +
                   'und dir wird eine Beschreibung in der Kopfzeile angezeigt. Um ' +
                   'zwischen den Kapiteln der Hilfe zu springen schau unter ' +
                   '"hier Hilfe finden".<br>Diese App wurde mit tools von ' +
                   '<a href="https://holoviz.org">HoloViz</a> realisiert.' +
                   '</p>')
        },
    
    # beginner mode help
    'help_beginner_mode':
        {
            'en': ('<div style="font-size:18px">beginner mode</div>' +
                   '<p style="margin-top: 0px;">' +
                   'In the beginner mode you can change four parameters of the model: ' +
                   'the slope and the widthprofile of the glacierbed, the ELA ' +
                   '(equilibrium line altitude) and the gradient of the mass balance profile.' +
                   'The changes are becoming visible in the figures after the ' +
                   '"run the model" button is clicked. In the beginner mode the ' +
                   'model will always start from zero and will run until it reached ' +
                   'equilibrium (volume stayed constant between two succeeding timesteps).' +
                   '</p>'),
            'de': ('<div style="font-size:18px">Anfänger</div>' +
                   '<p style="margin-top: 0px;">' +
                   'Hier können vier Parameter des Models verändert werden: die Hangneigung, ' +
                   'die Gletscherweite, die ELA (Gleichgewichtslinie) und der Gradient des ' +
                   'Massenbilanzprofils. Die Änderungen werden in den Diagrammen sichtbar ' +
                   'nachdem der "Model starten" Knopf gedrückt wird. Das Model startet ' +
                   'jedesmal von Null und läuft solange ' +
                   'bis ein Gleichgewicht erreicht wird (Volumen bleibt konstant zwischen ' +
                   'zwei aufeinanderfolgenden Zeitschritten).' +
                   '</p>')
        },
    
    # advanced mode help
    'help_advanced_mode_1':
        {
            'en': ('<div style="font-size:18px">advanced mode (I of II)</div>' +
                   '<p style="margin-top: 0px;">' +
                   'First lets look at the ' +
                   '"run the model" tab. Here you can change the ELA (equilibrium line ' +
                   'altitude), the gradient of the mass balance profile, Glen\'s creep ' +
                   'parameter, if there should be sliding at the glacierbed and the last ' +
                   'slider defines for how long the model should be running with the chosen ' +
                   'settings. In the advanced mode the model always continue from the current ' +
                   'glacier state. By clicking "advance model" the model will run for the ' +
                   'chosen years or with "run to equilibrium" the model runs until it ' +
                   'reaches equilibrium with the current settings (ignoring the last slider).'
                   '</p>'),
            'de': ('<div style="font-size:18px">Fortgeschritten (I von II)</div>' +
                   '<p style="margin-top: 0px;">' +
                   'Als erstes zum "Modellauf" tab. Hier können die ELA (Gleichgewichtslinie), ' +
                   'der Gradient des Massenbilanzprofils, der Glen\'s creep Parameter, das ' +
                   'Gleiten am Gletscherbed (Ja/Nein) und die länge des nächsten Modellaufs ' +
                   'eingestellt werden. Hier startet der Modellauf immer vom aktuellen ' +
                   'Modelstand. Mit "Model starten" läuft das Model für die ausgewählte ' +
                   'Dauer und mit "bis zum Gleichgewicht" läuft das Model bis es ' +
                   'im Gleichgewicht (konstantes Volumen) mit den gewählten Einstellungen ist.' +
                   '</p>')
        },
    
    'help_advanced_mode_2':
        {
            'en': ('<div style="font-size:18px">advanced mode (II of II)</div>' +
                   '<p style="margin-top: 0px;">' +
                   'Now looking at the "create new model" tab. Here you can start with a ' +
                   'new model by defining the width and the bedrock profile, if the linear profile is ' +
                   'selected also the slope can be defined. By ' +
                   'clicking the "create new model" button the changes are getting visible ' +
                   'in the figures and a new model with zero extend is initialised.'
                   '</p>'),
            'de': ('<div style="font-size:18px">Fortgeschritten (II von II)</div>' +
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
    'help_geometry_opt':
        {
            'en': ('<div style="font-size:18px">geometry options</div>' +
                   '<p style="margin-top: 0px;">' +
                   'Here you can switch additional colors in the geometry plot on and off. ' +
                   'In the top left figure the ice velocity, with a red colormap, and in the bottom left figure ' +
                   'the ice thickness, with a blue colormap, can be shown. The colorbars rearrange ' +
                   'the upper limit according to the ' +
                   'current maximum values (shown in info text of geometry plot). ' +
                   'The colors can be switched on after the model run or before it. ' +
                   'But when the colors are switched on during the model run the calculation ' +
                   'takes much longer.'
                   '</p>'),
            'de': ('<div style="font-size:18px">Geometrie optionen</div>' +
                   '<p style="margin-top: 0px;">' +
                   'Hier können zusätzlich Farbschatierungen in der "Geometrie Darstellung" ' +
                   'an- bzw. ausgeschaltet werden. Links oben kann die Eisgeschwindigkeit ' +
                   'und links unten die Eisdicke angezeigt werden. Beide Werte verwenden ' +
                   'die selbe Farbskala, welche auch hier gezeigt wird. Die Farbsakala ' +
                   'ist dabei dynamisch, das heißt das Maximum der Farbskala bezieht sich ' +
                   'auf die jeweiligen Maximalwerte welche im info text (rechts unten) ' +
                   'gezeigt werden. Die Farben können vor oder nach einem Modellauf ' +
                   'angezeigt werden. Modelläufe mit eingeschaltenen Farben benötigen ' +
                   'allerdings eine längere Rechenzeit.' +
                   '</p>')
        },
    
    # help page for timeseries options
    'help_timeseries_opt':
        {
            'en': ('<div style="font-size:18px">timeseries options</div>' +
                   '<p style="margin-top: 0px;">' +
                   'TODO' +
                   '</p>'),
            'de': ('<div style="font-size:18px">Zeitreihen optionen</div>' +
                   '<p style="margin-top: 0px;">' +
                   'TODO' +
                   '</p>')
        },
    
    # help page for model options
    'help_model_opt':
        {
            'en': ('<div style="font-size:18px">model options</div>' +
                   '<p style="margin-top: 0px;">' +
                   'In this section you can decide if the model should stop if the glacier is growing' +
                   'outside the domain, Moreover you can define how often the current model state should be ' +
                   'shown in the plots ("show model progress every ... years") and you can ' +
                   'define a upper limit of calculation years when the model runs to equilibrium ' +
                   '("maximum calculation year of model"). The changes came into operation after ' +
                   'clicking the "set new model options" button. The current settings are shown ' +
                   'in the text (bold numbers).'
                   '</p>'),
            'de': ('<div style="font-size:18px">Model optionen</div>' +
                   '<p style="margin-top: 0px;">' +
                   'Hier kann definiert werden wieoft der Modelstatus während dem Modellauf ' +
                   'angezeigt werden soll ("zeige Modelfortschritt alle ... Jahre") und ' +
                   'es kann eine obere Grenze für einen Modellauf festgelegt werden ' +
                   '("Maximale Laufzeit eines Modellaufs (Jahre)"). Die Änderungen werden ' +
                   'mit einem Klick auf "neue Optionen festlegen" wirksam. Die aktuellen ' +
                   'Einstellungen werden im Text gezeigt (fettgeschriebene Zahlen).' +
                   '</p>')
        },
    
    # help page for choose plots
    'help_choose_plots':
        {
            'en': ('<div style="font-size:18px">choose plots</div>' +
                   '<p style="margin-top: 0px;">' +
                   'Here you can decide which plots you want to use/should be updated. ' +
                   'So if you only are interested in one of the plots you can save ' +
                   'calculation time when only select the desired one. If one plot is ' +
                   'not selected this will be indicated on the plot.'
                   '</p>'),
            'de': ('<div style="font-size:18px">Darstellung wählen</div>' +
                   '<p style="margin-top: 0px;">' +
                   'Hier kann ausgewählt werden welche Darstellung benutzt/aktualisiert ' +
                   'werden soll. So kann Rechenzeit eingespart werden wenn man nur an ' +
                   'einer Darstellung interessiert ist. Wenn eine Darstellung nicht ' +
                   'aktiviert ist wird das in der Darstellung selbst angezeigt.' +
                   '</p>')
        },
    
    #help page for app options
    'help_app_opt':
        {
            'en': ('<div style="font-size:18px">app options</div>' +
                   '<p style="margin-top: 0px;">' +
                   'Here you can change the figure size of the upper row of the geometry plot ' +
                   '("scale figure size"), so you do not have to scroll to see all figures. ' +
                   'With "fontsize infotext" you can change the fontsize of the text in the ' +
                   'geometry plot. Additionally you can change the size of the whole app in ' +
                   'the browser window by pressing the "Strg" key and "+/-". Moreover here you ' +
                   'can change the bin width of the mass balance plot (geometry plot upper right).' +
                   '</p>'),
            'de': ('<div style="font-size:18px">App optionen</div>' +
                   '<p style="margin-top: 0px;">' +
                   'Mit "Darstellungsgröße skalieren" kann die Darstellungsgröße der oberen Reihe ' +
                   'der "Geometrie Darstellung" geändert werden, damit man nicht scrollen muss um ' +
                   'alle Bilder zu sehen. Mit "Schriftgröße Infotext" kann die Schriftgöße in der ' +
                   '"Geometrie Darstellung" angepasst werden, damit alle Informationen gelesen ' +
                   'werden können.' +
                   '</p>')
        },
    
    # help page for help panel
    'help_find_help_here':
        {
            'en': ('<div style="font-size:18px">find help here</div>' +
                   '<p style="margin-top: 0px;">' +
                   'With the buttons you can jump directly to one of the help pages you want ' +
                   'to know more about. (Also to this page here ;).)'
                   '</p>'),
            'de': ('<div style="font-size:18px">hier Hilfe finden</div>' +
                   '<p style="margin-top: 0px;">' +
                   'Mit den Knöpfen gelangt man direkt zu einzelnen Kapiteln der Hilfe. ' +
                   '(Auch zu dieser Seite hier ;).)'
                   '</p>')
        },
    
    # help for geometry plot
    'help_geometry_plot_1':
        {
            'en': ('<div style="font-size:18px">geometry plot (I of III)</div>' +
                   '<p style="margin-top: 0px;">' +
                   'The top left figure shows the glacierbed from the side in gray. ' +
                   'Underneath on the left the figure shows the glacier from above ' +
                   'and the dark gray areas indicate the boarder of the glacierbed.' +
                   'In both figures the dark blue line indicates the current glacier ' +
                   'state and if using the advanced mode also the previous state is ' +
                   'shown with a dashed line.' +
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
            'en': ('<div style="font-size:18px">geometry plot (II of III)</div>' +
                   '<p style="margin-top: 0px;">' +
                   'The top right figure shows the height dependent annual mass ' +
                   'balance as a black solid line with the upper x-axis. The dashed black ' +
                   'line shows the equilibrium line altitude (ELA, which is also shown in ' +
                   'the figures on the left).  If the plot is showing a glacier you can see ' +
                   'blue and red bins in this plot. The blue color is indicating a positive ' +
                   'mass balance (mass gain) and the red color is indicating a negative mass ' +
                   'balance (mass loss). The nuance contributes to the glacier wide mass balance ' +
                   'and the relative contribution of each bin can be seen in the colorbar to the ' +
                   'right of the figure.' +
                   '</p>'),
            'de': ('<div style="font-size:18px">Geometrie Darstellung (II von III)</div>' +
                   '<p style="margin-top: 0px;">' +
                   'Das Bild rechts oben zeigt die höhenabhängige jährliche Massenbilanz ' +
                   'als schwarze Linie. Die strichlierte Linie zeigt die Höhe der ELA an ' +
                   '(auch in den anderen zwei Bildern zu sehen). Grüne Flächen zeigen ' +
                   'einen Massengewinn am Gletscher an und rote Flächen einen ' +
                   'Massenverlust (länge der Balken zeigen relativen Anteil an). ' +
                   'Der Text unten rechts zeigt aktuelle Werte des Models an.'
                   '</p>')
        },
    
    'help_geometry_plot_3':
        {
            'en': ('<div style="font-size:18px">geometry plot (III of III)</div>' +
                   '<p style="margin-top: 0px;">' +
                   'The text ' +
                   'underneath shows statistics of the current glacier (model) state.' +
                   'If you want to zoom in you can do this by clicking into one of ' +
                   'the figures, hold the click and draw an rectangle. All figures ' +
                   'will rezoom automatically to the same extent. To go back to the ' +
                   'original extent click on the "Reset" button to the right of the ' +
                   'figures (two arrows forming a circle).' +
                   '</p>'),
            'de': ('<div style="font-size:18px">Geometrie Darstellung (III von III)</div>' +
                   '<p style="margin-top: 0px;">' +
                   'Wenn du hineinzoomen möchtest kannst du mit der Maus ein Rechteck ' +
                   'aufziehen (linke Maustaste gedrückt halten). Alle Bilder zoomen ' +
                   'automatisch auf den gleichen Ausschnitt. Um den Zoom rückgängig ' +
                   'zu machen auf "Reset" rechts neben den Bildern drücken (zwei ' +
                   'Pfeile welche einen Kreis formen).' +
                   '</p>')
        },
    
    # help page for timeseries plot
    'help_timeseries_plot_1':
        {
            'en': ('<div style="font-size:18px">timeseries plot (I of II)</div>' +
                   '<p style="margin-top: 0px;">' +
                   'The three figures on top show the evolution of the volume, area ' +
                   'and length with time. The resolution of the figures (how ' +
                   'often the state is shown) depends on the model settings (see ' +
                   '"model options"). After the model run has finished the section ' +
                   'gets a number and some model settings and statistics are shown ' +
                   'in the table below. The figures and the table are cleared ' +
                   'when a new model is initialized.' +
                   '</p>'),
            'de': ('<div style="font-size:18px">Zeitreihen Darstellung (I von II)</div>' +
                   '<p style="margin-top: 0px;">' +
                   'Die drei Bilder rechts zeigen die zeitlichen Verläufe der Länge, Fläche und ' +
                   'Volumen. Die Auflösung hängt dabei von den aktuellen Modeleinstellungen ab ' +
                   '(siehe "Modeloptionen"). Wenn ein Modellauf beendet wurde bekommt der ' +
                   'Abschnitt eine Nummer und es werden Modeleinstellungen und Endwerte ' +
                   'des Models in der Tabelle rechts angezeigt. Die Bilder und die Tabelle ' +
                   'werden gelöscht wenn ein neues Model gestartet wird.'
                   '</p>')
        },
    
    'help_timeseries_plot_2':
        {
            'en': ('<div style="font-size:18px">timeseries plot (II of II)</div>' +
                   '<p style="margin-top: 0px;">' +
                   'You can zoom in and out on the plots by using the mousewheel ' +
                   'and you can use a mouseclick to drag the plots around. If you ' +
                   'zoom in on one plot the other plot will automatically rezoom ' +
                   'to the same time span. When moving with the mouse over the curves ' +
                   'a hover will show you the exact values of the points. To go back ' +
                   'to the original extent click on the "Reset" button to the left of ' +
                   'the figures (two arrows forming a circle).'
                   '</p>'),
            'de': ('<div style="font-size:18px">Zeitreihen Darstellung (II von II)</div>' +
                   '<p style="margin-top: 0px;">' +
                   'Mit dem Mausrad kann in die Bilder hineingezoomt werden und mit einem ' +
                   'Mausklick kann der Bildausschnitt verschoben werden. Alle Änderungen ' +
                   'des Bildausschnitts werden automatisch auf den anderen Bildern ' +
                   'aktualisiert. Mit "Reset" (zwei Pfeile welche einen Kreis formen) ' +
                   'links von den Bildern kann der Zoom rückgängig gemacht werden. ' +
                   'Wenn man mit dem Mauszeiger über die Kurven fährt ' +
                   'werden die genauen Werte der Zeitschritte angezeigt.'
                   '</p>')
        },
    
    # label for next button
    'next_button_text':
        {
            'en': 'next',
            'de': 'weiter'
        },
    
    # label for previous button
    'previous_button_text':
        {
            'en': 'previous',
            'de': 'zurück'
        },
}

# text for panels and their widgets
panel_text = {
    # beginner mode and advanced mode panels
    
    # options for bedrock profil, do not change order, first entry is default
    'bed_rock_profil_values':
        {
            'en': ['linear', 'getting flatter', 'getting steeper', 'cliff'],
            'de': ['linear', 'flächer werdend', 'steiler werdend', 'Klippe']
        },
    
    # options for bedrock width, do not change order, first entry is default
    'bed_rock_width_values':
        {
            'en': ['constant', 'getting narrower', 'getting wider',
                   'wide top, narrow bottom'],
            'de': ['konstant', 'enger werden', 'breiter werden',
                   'oben weit, unten eng']
        },
    
    # options for glens creep parameter, do not change order, second entry is default
    'glens_creep_parameter_values':
        {
            'en': ['small', 'medium', 'large'],
            'de': ['klein', 'mittel', 'groß']
        },
    
    # options for sliding, do not change order, first entry is default
    'sliding_parameter_values':
        {
            'en': ['no sliding', 'sliding'],
            'de': ['kein Gleiten', 'Gleiten']
        },
    
    # names for select widgets
    'bed_rock_slope_beginner_heading':
        {
            'en': 'slope of bedrock profile',
            'de': 'Hangneigung'
        },
    
    'bed_rock_slope_advanced_heading':
        {
            'en': 'slope of linear bedrock profile',
            'de': 'Hangneigung (lineares Untergrundprofil)'
        },
    
    'bed_rock_width_heading':
        {
            'en': 'width along glacier',
            'de': 'Gletscherweite'
        },
    
    'mb_gradient_heading':
        {
            'en': 'mass balance gradient',
            'de': 'Massenbilanzgradient'
        },
    
    'ELA_height_heading':
        {
            'en': 'ELA (equilibrium line altitude)',
            'de': 'ELA (Gleichgewichtslinie)'
        },
    
    'beginner_button_heading':
        {
            'en': 'run the model',
            'de': 'Model starten'
        },
    
    'bed_rock_profil_heading':
        {
            'en': 'bedrock profile',
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
            'de': 'gleiten'
        },
    
    'years_to_advance_model_heading':
        {
            'en': 'years to advance model',
            'de': 'Jahre für Modellauf'
        },
    
    'button_for_equilibrium_run_heading':
        {
            'en': 'run to equilibrium',
            'de': 'bis zum Gleichgewicht'
        },
    
    'button_to_advance_for_some_years_heading':
        {
            'en': 'advance model',
            'de': 'Model starten'
        },
    
    'button_to_create_new_model_heading':
        {
            'en': 'create new model',
            'de': 'neues Model'
        },
    
    # headings for advanced mode tabs
    'run_model_tab_heading':
        {
            'en': 'run the model',
            'de': 'Modellauf'
        },
    
    'create_new_model_tab_heading':
        {
            'en': 'create new model',
            'de': 'neues Model'
        },
    
    # geometry options panel
    
    'show_velocity_heading':
        {
            'en': 'ice velocity (top left)',
            'de': 'Eisgeschwindigkeit (oben links)'
        },
    
    'show_thickness_heading':
        {
            'en': 'ice thickness (bottom left)',
            'de': 'Eisdicke (unten links)'
        },
    
    'geometry_opt_description':
        {
            'en': ('<p style="margin-top: 0px;">Here you can choose if the velocity or/and the thickness ' +
                   'of the ice should be shown in the geometry plot. The colorbar shows the intervals, ' +
                   'maximum refers to the value shown in the "info text" (bottom right geometry plot).</p> '),
            'de': ('<p style="margin-top: 0px;">Hier kann ausgewählt werden ob die Eisgeschwindigkeit ' +
                   'und/oder die Eisdicke als Farbe angezeigt werden soll (im Geometrie Darstellung). ' +
                   'Die gezeigte Farbskala ' +
                   'bezieht sich auf die maximal Werte im "info Text" (unten rechts Geometrie ' +
                   'Darstellung). </p>')
        },
    
    'mb_curve_bin_width_heading':
        {
            'en': 'min bin width of mb plot (top right)',
            'de': 'min bin weite mb plots (rechts oben)'
        },
    
    # timeseries opt panel
    
    'top_axis_heading':
        {
            'en': 'top axis',
            'de': 'obere Achse'
        },
    
    'middle_axis_heading':
        {
            'en': 'middle axis',
            'de': 'mittlere Achse'
        },
    
    'bottom_axis_heading':
        {
            'en': 'bottom axis',
            'de': 'untere Achse'
        },
    
    # options for timeseries plots, do not change order, first three entries are default
    'timeseries_axis_options':
        {
            'en': ['volume', 'area', 'length','max velocity', 
                   'max thickness', 'max ice flux'],
            'de': ['Volumen', 'Fläche', 'Länge', 'max Geschwindigkeit', 
                   'max Dicke', 'max Eisfluss']
        },
    
    # panel for model options
    
    'stop_if_outside_heading':
        {
            'en': 'stop run if glacier outside of domain',
            'de': 'stop wenn Gletscher außerhalb'
        },
    
    'toggle_buttons_checkbox_heading':
        {
            'en': 'toggle buttons during run',
            'de': 'Buttons umschalten während Modellauf'
        },
    
    'toggle_buttons_button_heading':
        {
            'en': 'toggle buttons',
            'de': 'Buttons umschalten'
        },
    
    'dyears_model_slider_heading':
        {
            'en': 'show model progress every .. years',
            'de': 'zeige Modelfortschritt alle .. Jahre'
        },
    
    'max_calc_years_slider_heading':
        {
            'en': 'abort model after .. years',
            'de': 'Model abbrechen nach .. Jahren'
        },
    
    'current_model_options_text':
        {
            'en': ('Model currently showing progress every **{}** years and ' +
                   'abort model after **{}** years of calculation'),
            'de': ('Model zeigt zurzeit Fortschritt alle **{}** Jahre und ' +
                   'Modellauf wird nach **{}** Jahren abgebrochen.')
        },
    
    'set_model_options_heading':
        {
            'en': 'set new model options',
            'de': 'neue Optionen festlegen'
        },
    
    # choose plots panel
    
    'show_geometry_plot_heading':
        {
            'en': 'show geometry plot',
            'de': 'zeige Geometrie Darstellung'
        },
    
    'show_timeseries_plot_heading':
        {
            'en': 'show timeseries plot',
            'de': 'zeige Zeitreihen Darstellung'
        },
    
    'choose_plots_description':
        {
            'en': ('Here you can choose which plot should be updated with the model runs. ' +
                   'The more plots are choosen, the longer the computational time. Here ' +
                   'also the width of the table could be changed to fit your screen size.'),
            'de': ('Hier can ausgewählt werden welche Darstellungen mit den Modelläufen ' +
                   'aktualisiert werden sollen. Umso mehr Darstellungen ausgewählt sind, ' +
                   'umso länger die Rechenzeit des Models. Außerdem kann hier die Breite ' +
                   'der Tabelle eingestellt werden.')
        },
    
    # app opt panel
    
    'geometry_figure_size_heading':
        {
            'en': 'scale figure size',
            'de': 'Darstellungsgröße skalieren'
        },
    
    'geometry_figure_fontsize':
        {
            'en': 'fontsize infotext',
            'de': 'Schriftgröße Infotext'
        },
    
    'app_options_description':
        {
            'en': ('Here you can change the geometry plot figure size, the font size ' +
                   'of the geometry plot infotext (bottom right) and the number of shown ' +
                   'table rows.'),
            'de': ('Hier kann die Darstellungsgröße der geometrie darstellung, ' +
                   'die Schriftgröße des Infotextes und die Anzahl der Tabellenzeilen geändert ' +
                   'werden.')
        },
    
    # help panel
    
    'help_panel_description':
        {
            'en': ('<p style="margin-top: 0px;">Click on button to get help shown in ' +
                   'Headerline. Navigate with "next" and "previous" button (on the right).' +
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
            'en': 'beginner mode',
            'de': 'Anfänger'
        },
    
    'advanced_mode':
        {
            'en': 'advanced mode',
            'de': 'Fortgeschritten'
        },
    
    'choose_plots':
        {
            'en': 'choose plots',
            'de': 'Plots wählen'
        },
    
    'geometry_opt':
        {
            'en': 'geometry opt.',
            'de': 'Geometrie opt.'
        },
    
    'timeseries_opt':
        {
            'en': 'timeseries opt.',
            'de': 'Zeitreihen opt.'
        },
    
    'model_opt':
        {
            'en': 'model opt.',
            'de': 'Model opt.'
        },
    
    'app_opt':
        {
            'en': 'app opt.',
            'de': 'App opt.'
        },
    
    'find_help_here':
        {
            'en': 'find help here',
            'de': 'Hilfe hier'
        },
}

# labels for geometry plot
geometry_plot_labels = {
    'bedrock_x_label':
        {
            'en': 'distance along glacier (km)',
            'de': 'Distanz entlang des Gletschers (km)'
        },
    
    'bedrock_height_y_label':
        {
            'en': 'altitude (m)',
            'de': 'Höhe (m)'
        },
    
    'bedrock_width_y_label':
        {
            'en': 'width (m)',
            'de': 'Weite (m)'
        },
    
    'glacier_label':
        {
            'en': 'glacier',
            'de': 'Gletscher'
        },
    
    'mb_x_label':
        {
            'en': 'annual mass balance (mm w.e./year)',
            'de': 'jährliche Massenbilanz (mm w.e/Jahr)'
        },
    
    'area_x_label':
        {
            'en': 'area',
            'de': 'Fläche'
        },
    
    'mb_label':
        {
            'en': 'mass balance',
            'de': 'Massenbilanz'
        },
    
    'info_text_new_model':
        {
            'en': 'New Model geometry\ninitialised',
            'de': 'Neue Model Geometry\ninitialisiert'
        },
    
    'info_text_switched_off':
        {
            'en': 'This plot is currently not used/updated.\nTo switch it on go to "choose plots".',
            'de': 'Dieses Diagramm ist aktuell nicht aktiv\nAktivieren unter "Darstellung wählen"'
        },
    
    'info_text_switched_on':
        {
            'en': 'Plot is switched on again\nand will be updated with the next run!',
            'de': 'Diagramm ist aktiv und\n wird mit nächstem Modellauf aktualisiert'
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
            'en': 'Model stopped (max calculation time reached, see "model options")',
            'de': 'Modellauf abgebrochen (maximale Zeit erreicht, siehe "Modeloptionen")'
        },
    
    'info_text_outside_domain':
        {
            'en': 'Model stopped (glacier outside of domain, see "model options")',
            'de': 'Modellauf abgebrochen (Gletscher außerhalb der Domäne, siehe "Modeloptionen")'
        },
    
    'info_text_statistics':
        {
            'en': ('\nTime: {:4.0f} years     Length: {:4.2f} km      Area: {:.2f} km²     Volume: {:.2f} km³\n'
                   'Max ice thickness: {:.0f} m          Max ice velocity: {:.0f} m/year\n'
                   'Glacier-wide mass-balance (mb): {:.2} mm w.e./year'),
            'de': ('\nZeit: {:4.0f} years     Länge: {:4.2f} km      Fläche: {:.2f} km²     Volumen: {:.2f} km³\n'
                   'Max Eisdicke: {:.0f} m          Max Eisgeschwindigkeit: {:.0f} m/year\n'
                   'Gletscherweite Massenbilanz (mb): {:.2} mm w.e./year')
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
    
    'plot_active':
        {
            'en': 'plot is ready to use \nand update with the next run',
            'de': 'Diagramm bereit und\nwird mit nächstem Modellauf aktualisiert'
        },
    
    'plot_unactive':
        {
            'en': 'plot is switched off \nto switch on look at "choose plots"',
            'de': 'Diagramm nicht aktiv\nAktivieren unter "Diagramm wählen"'
        },
}

# labels for timeseries table
timeseries_table_labels = {
    'table_heading_1':
        {
            'en': ['Profil', 'Slope (°)', 'width', 'ELA (m)',
                   'gradient (mm w.e./year/m)', 'Glen\'s creep',
                   'sliding', 'Years'],
            'de': ['Untergrundprofil', 'Hangneigung (°)', 'Gletscherweite',
                   'ELA (m)', 'Gradient (mm w.e./Jahr/m)',
                   'Glen\'s creep', 'Gleiten', 'Jahre']
        },
    
    'table_heading_2':
        {
            'en': ['in equilibrium', 'outside domain'],
            'de': ['im Gleichgewicht', 'außerhalb der Domäne']
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
            'en': 'geometry plot',
            'de': 'Geometrie Darstellung'
        },
    
    'timeseries_plot':
        {
            'en': 'timeseries plot',
            'de': 'Zeitreihen Darstellung'
        },
}