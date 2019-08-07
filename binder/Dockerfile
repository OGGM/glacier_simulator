FROM oggm/r2d:20190807T1138

# enable nbserverproxy
RUN jupyter serverextension enable --sys-prefix nbserverproxy
# install the panel server extension so that
# panel launches at startup
RUN mv panelserverextension.py ${NB_PYTHON_PREFIX}/lib/python*/site-packages/
# enable panel extension
RUN jupyter serverextension enable --sys-prefix panelserverextension
# ensure matplotlib uses agg backend
RUN mkdir $HOME/.config
RUN mkdir $HOME/.config/matplotlib
RUN echo 'backend : Agg' > $HOME/.config/matplotlib/matplotlibrc

