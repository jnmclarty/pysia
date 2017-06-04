# -*- coding: utf-8 -*-

import requests as r

GET = 1
POST = 2

class Sia(object):
    def __init__(self, host='http://localhost', port='1234'):
        self.host = host
        self.port = port
    @property
    def _url_base(self):
        return self.host + ":" + str(self.port)
    def __call__(self, verb, url, data=None):
        full_url = self._url_base + url
        if verb == GET:
            return r.get(full_url, params=data)
        elif verb == POST:
            out = r.post(full_url, data=data)
            "TODO: Raise exception for users on bad status code"
            return out

    def get_consensus(self, **data):
        url = '/consensus'
        return self(GET, url, data)

    def set_consensus_validate_transactionset(self, **data):
        url = '/consensus/validate/transactionset'
        return self(POST, url, data)

    def get_daemon_constants(self, **data):
        url = '/daemon/constants'
        return self(GET, url, data)

    def get_daemon_stop(self, **data):
        url = '/daemon/stop'
        return self(GET, url, data)

    def get_daemon_version(self, **data):
        url = '/daemon/version'
        return self(GET, url, data)

    def get_gateway(self, **data):
        url = '/gateway'
        return self(GET, url, data)

    def set_gateway_connect(self, netaddress, **data):
        url = '/gateway/connect/{netaddress}'.format(netaddress=netaddress)
        return self(POST, url, data)

    def set_gateway_disconnect(self, netaddress, **data):
        url = '/gateway/disconnect/{netaddress}'.format(netaddress=netaddress)
        return self(POST, url, data)

    def get_host(self, **data):
        url = '/host'
        return self(GET, url, data)

    def set_host(self, **data):
        url = '/host'
        return self(POST, url, data)

    def set_host_announce(self, **data):
        url = '/host/announce'
        return self(POST, url, data)

    def get_host_storage(self, **data):
        url = '/host/storage'
        return self(GET, url, data)

    def set_host_storage_folders_add(self, **data):
        url = '/host/storage/folders/add'
        return self(POST, url, data)

    def set_host_storage_folders_remove(self, **data):
        url = '/host/storage/folders/remove'
        return self(POST, url, data)

    def set_host_storage_folders_resize(self, **data):
        url = '/host/storage/folders/resize'
        return self(POST, url, data)

    def set_host_storage_sectors_delete(self, merkleroot, **data):
        url = '/host/storage/sectors/delete/{merkleroot}'.format(merkleroot=merkleroot)
        return self(POST, url, data)

    def get_hostdb_active(self, **data):
        url = '/hostdb/active'
        return self(GET, url, data)

    def get_hostdb_all(self, **data):
        url = '/hostdb/all'
        return self(GET, url, data)

    def get_hostdb_hosts(self, pubkey, **data):
        url = '/hostdb/hosts/{pubkey}'.format(pubkey=pubkey)
        return self(GET, url, data)

    def get_miner(self, **data):
        url = '/miner'
        return self(GET, url, data)

    def get_miner_header(self, **data):
        url = '/miner/header'
        return self(GET, url, data)

    def set_miner_header(self, **data):
        url = '/miner/header'
        return self(POST, url, data)

    def get_miner_start(self, **data):
        url = '/miner/start'
        return self(GET, url, data)

    def get_miner_stop(self, **data):
        url = '/miner/stop'
        return self(GET, url, data)

    def get_renter(self, **data):
        url = '/renter'
        return self(GET, url, data)

    def set_renter(self, **data):
        url = '/renter'
        return self(POST, url, data)

    def get_renter_contracts(self, **data):
        url = '/renter/contracts'
        return self(GET, url, data)

    def set_renter_delete(self, siapath, **data):
        url = '/renter/delete/{siapath}'.format(siapath=siapath)
        return self(POST, url, data)

    def get_renter_download(self, siapath, **data):
        url = '/renter/download/{siapath}'.format(siapath=siapath)
        return self(GET, url, data)

    def get_renter_downloadasync(self, siapath, **data):
        url = '/renter/downloadasync/{siapath}'.format(siapath=siapath)
        return self(GET, url, data)

    def get_renter_downloads(self, **data):
        url = '/renter/downloads'
        return self(GET, url, data)

    def get_renter_files(self, **data):
        url = '/renter/files'
        return self(GET, url, data)

    def get_renter_prices(self, **data):
        url = '/renter/prices'
        return self(GET, url, data)

    def set_renter_rename(self, siapath, **data):
        url = '/renter/rename/{siapath}'.format(siapath=siapath)
        return self(POST, url, data)

    def set_renter_upload(self, siapath, **data):
        url = '/renter/upload/{siapath}'.format(siapath=siapath)
        return self(POST, url, data)

    def get_wallet(self, **data):
        url = '/wallet'
        return self(GET, url, data)

    def set_wallet_033x(self, **data):
        url = '/wallet/033x'
        return self(POST, url, data)

    def get_wallet_address(self, **data):
        url = '/wallet/address'
        return self(GET, url, data)

    def get_wallet_addresses(self, **data):
        url = '/wallet/addresses'
        return self(GET, url, data)

    def get_wallet_backup(self, **data):
        url = '/wallet/backup'
        return self(GET, url, data)

    def set_wallet_init(self, **data):
        url = '/wallet/init'
        return self(POST, url, data)

    def set_wallet_init_seed(self, **data):
        url = '/wallet/init/seed'
        return self(POST, url, data)

    def set_wallet_lock(self, **data):
        url = '/wallet/lock'
        return self(POST, url, data)

    def set_wallet_seed(self, **data):
        url = '/wallet/seed'
        return self(POST, url, data)

    def get_wallet_seeds(self, **data):
        url = '/wallet/seeds'
        return self(GET, url, data)

    def set_wallet_siacoins(self, **data):
        url = '/wallet/siacoins'
        return self(POST, url, data)

    def set_wallet_siafunds(self, **data):
        url = '/wallet/siafunds'
        return self(POST, url, data)

    def set_wallet_siagkey(self, **data):
        url = '/wallet/siagkey'
        return self(POST, url, data)

    def set_wallet_sweep_seed(self, **data):
        url = '/wallet/sweep/seed'
        return self(POST, url, data)

    def get_wallet_transaction(self, id, **data):
        url = '/wallet/transaction/{id}'.format(id=id)
        return self(GET, url, data)

    def get_wallet_transactions(self, addr=None, **data):
        url = '/wallet/transactions/{addr}'.format(addr=addr)
        return self(GET, url, data)

    def set_wallet_unlock(self, **data):
        url = '/wallet/unlock'
        return self(POST, url, data)


if __name__ == '__main__':
    sc = Sia()
    sc.get_consensus()
