require 'test_helper'

class ClosetsControllerTest < ActionDispatch::IntegrationTest
  setup do
    @closet = closets(:one)
  end

  test "should get index" do
    get closets_url
    assert_response :success
  end

  test "should get new" do
    get new_closet_url
    assert_response :success
  end

  test "should create closet" do
    assert_difference('Closet.count') do
      post closets_url, params: { closet: { location: @closet.location, name: @closet.name, user_id: @closet.user_id } }
    end

    assert_redirected_to closet_path(Closet.last)
  end

  test "should show closet" do
    get closet_url(@closet)
    assert_response :success
  end

  test "should get edit" do
    get edit_closet_url(@closet)
    assert_response :success
  end

  test "should update closet" do
    patch closet_url(@closet), params: { closet: { location: @closet.location, name: @closet.name, user_id: @closet.user_id } }
    assert_redirected_to closet_path(@closet)
  end

  test "should destroy closet" do
    assert_difference('Closet.count', -1) do
      delete closet_url(@closet)
    end

    assert_redirected_to closets_path
  end
end
