//
// Copyright Aliaksei Levin (levlam@telegram.org), Arseny Smirnov (arseny30@gmail.com) 2014-2019
//
// Distributed under the Boost Software License, Version 1.0. (See accompanying
// file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
//
#pragma once

#include "td/actor/actor.h"
#include "td/actor/PromiseFuture.h"

#include "td/telegram/files/FileStats.h"

namespace td {

class FileStatsWorker : public Actor {
 public:
  explicit FileStatsWorker(ActorShared<> parent) : parent_(std::move(parent)) {
  }
  void get_stats(bool need_all_files, bool split_by_owner_dialog_id, Promise<FileStats> promise);

 private:
  ActorShared<> parent_;
};

}  // namespace td
