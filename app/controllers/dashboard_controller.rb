class DashboardController < ApplicationController
  before_filter :set_user

  def index
    @closets = @user.closets.limit(8)
    @items = @user.items
  end

  private
    def set_user
      @user = current_user
    end

end
