from dotenv import load_dotenv
from os import getenv

import pymongo
import pymongo.collection
import pymongo.cursor
import pymongo.database

load_dotenv()
client: pymongo.MongoClient = pymongo.MongoClient(
    host="mongodb://ticket_db:27017/",
    username=getenv("MONGO_INITDB_ROOT_USERNAME"),
    password=getenv("MONGO_INITDB_ROOT_PASSWORD")
    )
ticket_db = client["ticket_db"]

class ticket_tab:
    """Constructor of each server table.

        Attributes
        ----------
        thread_id : `int`
            Id of thread.
        owner : `str`
            Username of thread owner.
        owner_id : `int`
            User id of thread owner.
        private : `bool`
            Thread visibility `True` if it's private.
        status : `bool`
            `True` if this thread still active.
        participant : `list`
            List of username who've interact in this thread.
    """
    def __init__(self, server_id : int) -> None:
        server_id = str(server_id)
        if not server_id in ticket_db.list_collection_names():
            new_collec = ticket_db[server_id]
            new_collec.insert_one(
                {
                    "thread_id" : -1,
                    "owner" : "Bob",
                    "owner_id" : "0",
                    "private" : True,
                    "status" : True,
                    "participant" : ["Alice"]
                })
            self.collection = new_collec
            self.collection.delete_one({"thread_id" : -1})
        else:
            self.collection = ticket_db[server_id]

    def ft_ins_thread(self, tid : int, username : str, \
                        user_id : int, private : bool,\
                        status : bool, participant : list) -> None:
        """call after create thread"""
        participant.append(username)
        self.collection.insert_one(
                {
                    "thread_id" : tid,
                    "owner" : username,
                    "owner_id" : user_id,
                    "private" : private,
                    "status" : status,
                    "participant" : participant
                })
    
    def ft_update_participant(self, tid : int, username : str) -> None:
        """update participant list"""
        rec = self.collection.find_one({"thread_id" : tid}, {})
        if not rec or rec == None:
            return
        par_list : list = rec["participant"]
        if not username in par_list:
            par_list.append(username)
            self.collection.update_one(
                {"thread_id" : tid}, { "$set" : {"participant" : par_list}}
            )

    def ft_close_thread(self, tid : int) -> None:
        """update thread status"""
        self.collection.update_one(
            {"thread_id" : tid}, { "$set" : {"status" : False}}
        )

    def ft_get_by_thread(self, tid : int) -> dict:
        """get specific record by id"""
        return self.collection.find_one({"thread_id" : tid})

    def ft_get_by_user(self, user_id : int) -> list:
        """get specific record by user"""
        return self.collection.find({"owner_id" : user_id}, {"_id" : False}).to_list()

    def ft_get_by_stat(self, status : bool) -> list:
        """get specific record by open/closed"""
        return self.collection.find({"status" : status }, {"_id" : False}).to_list()

    def ft_get_all(self) -> list:
        """get record of all thread in the server"""
        return self.collection.find({}, {"_id": False}).to_list()

    def ft_clear(self) -> None:
        """clear all record in table"""
        self.collection.delete_many({})
