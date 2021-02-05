template = """
{% extends base %}

<!-- goes in body -->
{% block postamble %}
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.6.0/css/bootstrap.min.css">
{% endblock %}

<!-- goes in body -->
{% block contents %}
<div class="container-float">
  <div class="row">
    <div class="col">
      {{ embed(roots.header) }}
    </div>
  </div>
  <div class="row">
    <div class="col">
      {{ embed(roots.menu_and_figures) }}
    </div>
  </div>
</div>
{% endblock %}
"""
