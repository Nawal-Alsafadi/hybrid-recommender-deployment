from flask import request, jsonify, make_response
from api.middle_wares.num_recommends_params import extract_num_recommends_params
from api.middle_wares.user_id_params import extract_user_id_params
from api.models.recommendation_model.main_recommendation_model.stage_advanved.collaborative_recommender import \
    CollaborativeRecommender
from api.models.recommendation_model.main_recommendation_model.stage_advanved.hybrid_recommender import HybridRecommender
@extract_num_recommends_params
@extract_user_id_params
def get_hybrid_recommends(user_id, num_recommendations):
    try:
        collaborative_recommender = CollaborativeRecommender()
        data = collaborative_recommender.read_results()
        collaborative_result = CollaborativeRecommender.recommend_items(user_id=user_id, predictions=data, num_recommendations=20 )
        hybrid_recommender = HybridRecommender()
        similarity_matrix = hybrid_recommender.read_results()
        result = hybrid_recommender.hybrid_recommendes(similarity_matrix=similarity_matrix, user_id=user_id, item_list=collaborative_result, num_recommendations=num_recommendations )
        return make_response(jsonify({
            "message": "Recommendation completed successfully.",
            "success": True,
            "products_ids": result
        })), 200
    except Exception as e:
        error_message = f"Error: {str(e)}"
        return make_response(jsonify({
            "message": "Something went wrong. We're working to solve it.",
            "success": False,
            "error": error_message
        }), 500)