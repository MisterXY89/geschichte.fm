docker exec -it pg_container bash
# psql --host=pg_container --dbname=test_db --username=root
psql -h pg_container -d test_db -U root -f create_table.psql


https://adn.podigee-cdn.net/adswizz/media/podcast_47771_geschichten_aus_der_geschichte_episode_543026_gag02_tatortschau_mit_wiedererkennungswert.mp3?awCollectionId=svo_3857a7&awEpisodeId=543026&source=webplayer-download&v=1632126427