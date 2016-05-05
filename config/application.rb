require File.expand_path('../boot', __FILE__)

require 'rails/all'

# Require the gems listed in Gemfile, including any gems
# you've limited to :test, :development, or :production.
Bundler.require(*Rails.groups)

module Whatwear
  class Application < Rails::Application
    # Settings in config/environments/* take precedence over those specified here.
    # Application configuration should go into files in config/initializers
    config.generators do |g|
      g.orm             :active_record
      g.stylesheets     false
      g.javascripts     false
      g.template_engine :haml
    end   # -- all .rb files in that directory are automatically loaded.
    config.action_view.field_error_proc = Proc.new { |html_tag, instance|
      "<div class=\"field error\">#{html_tag}</div>".html_safe
    }
  end
end
